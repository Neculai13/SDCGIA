"""Reia cereri salvate; implicit doar verificare offline, fara generare."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def request_for(row):
    options=dict(row['options'])
    if row['backend']=='ollama':
        body={'model':row['model'],'prompt':row['prompt'],'system':row['system'],
              'stream':False,'options':options}
        if row.get('think') is not None:body['think']=row['think']
        return '/api/generate',body
    return '/v1/chat/completions',dict(options,model=row['model'],stream=False,
        messages=[{'role':'system','content':row['system']},
                  {'role':'user','content':row['prompt']}])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model',required=True)
    p.add_argument('--limit',type=int,default=1)
    p.add_argument('--url',default=None)
    p.add_argument('--run',action='store_true')
    args=p.parse_args()
    if args.limit<1:p.error('--limit trebuie sa fie pozitiv')
    root=Path(__file__).resolve().parent
    rows=[json.loads(x) for x in (root/'prompturi.jsonl').read_text(encoding='utf-8').splitlines()]
    selected=[r for r in rows if r['model']==args.model][:args.limit]
    if not selected:p.error('Model absent; consulta modele_setari.json')
    for row in selected:
        route,body=request_for(row)
        print(row['id'],row['backend'],row['model'],'- cerere verificata')
        if not args.run:continue
        url=args.url or ('http://127.0.0.1:11434' if row['backend']=='ollama' else None)
        if not url:p.error('Pentru llama.cpp indica --url cu serverul local')
        parsed=urlparse(url)
        if parsed.scheme!='http' or parsed.hostname not in {'127.0.0.1','localhost','::1'} or parsed.username or parsed.password:
            p.error('Este acceptat doar un server HTTP local, fara credentiale in URL')
        folder=root/'rezultate_noi'
        folder.mkdir(exist_ok=True)
        path=folder/(hashlib.sha256(row['id'].encode()).hexdigest()[:24]+'.json')
        if path.exists():
            print('Exista deja; nu suprascriu:',path.name)
            continue
        req=Request(url.rstrip('/')+route,data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
        with urlopen(req,timeout=1800) as response:result=json.load(response)
        text=result.get('response','') if row['backend']=='ollama' else result['choices'][0]['message']['content']
        # Exclusiv un fisier nou; nu modifica prompturile sau rezultatele experimentului.
        with path.open('x',encoding='utf-8') as f:
            json.dump({'request':row,'text':text,'raw_response':result},f,ensure_ascii=False,indent=2)
        print('Salvat:',path.name)


if __name__=='__main__':main()
