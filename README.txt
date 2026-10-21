SDCGIA - Detectarea textelor umane si generate de AI
Tema 6: Decision model cu Unsloth

Continut:
  notebook.ipynb - antrenare, calibrare si evaluare automata in Colab
  generare/ - codul de generare, modelele, prompturile si setarile folosite
  rezultate/ - rezultate globale si per model-sursa, pentru cele doua experimente
  raport.pdf - descrierea implementarii, rezultatele si limitele
  date/SDCGIA_human_ai_v1.zip - datele de antrenare, calibrare si test
  date/supplementary_evaluation.zip - textele lotului suplimentar deja generat

Detector: Unsloth Qwen3.5-4B, ajustat cu LoRA, antrenat si evaluat in Colab pe T4.
Corpus: 3.767 texte human si 2.590 texte AI.
Test principal: 952/954 clasificari corecte (99,79%), cu 1 FP si 1 FN.
Test suplimentar: 150/150 corecte, pe 30 surse noi, cu doua modele si doua
profiluri de sampling. Acest rezultat se raporteaza separat de testul principal.

Rulare in Colab:
  https://colab.research.google.com/github/Neculai13/SDCGIA/blob/main/notebook.ipynb

  1. Deschide linkul intr-o sesiune noua.
  2. Selecteaza Runtime > Change runtime type > T4 GPU.
  3. Apasa Runtime > Run all.

Notebookul descarca singur ambele arhive din GitHub si verifica hash-urile.
Nu necesita Ollama, generare locala, incarcari manuale sau fisierele noastre din
Google Drive. Instaleaza versiunile principale fixate, antreneaza de la zero un
LoRA nou, calibreaza si evalueaza pe cele doua loturi. Modelul de baza se descarca
din Hugging Face. Disponibilitatea GPU si accesul la descarcari depind de Colab.

Rularea poate dura cateva ore. Rezultatele se scriu intr-un director nou din
/content/SDCGIA/runs/ si se descarca la final ca experiment_colab.zip, impreuna
cu modelul calibrat. /content este temporar; o sesiune intrerupta poate pierde
fisierele. Nu se suprascriu rezultatele istorice din acest repository.

Aceasta versiune a notebookului are verificarile locale de cod si date facute,
dar nu a fost inca rerulata integral pe un GPU nou. Pot fi necesare ajustari daca
mediul Colab sau dependentele nu mai sunt compatibile. Nu este garantata obtinerea
exact a scorurilor istorice de mai sus.

Arhiva principala are 4,35 MiB; modelul salvat istoric nu este inclus.
Arhiva contine textele in formatul modelului si metadatele pentru cele trei
partitii: train 4.448, calibration 955, test 954. Numele v1 al bundle-ului este
cel folosit si de notebookul adaptat; nu indica un alt corpus.
Articolele integrale din arhiva isi pastreaza drepturile surselor originale.

Generare locala optionala, pentru alte texte (nu este necesara rularii Colab):
Python 3.12; modelele trebuie instalate separat.
  python generare/genereaza.py --model qwen3.5:0.8b --limit 1
Comanda verifica cererea, fara a genera. Pentru generare reala se adauga --run.
Ollama foloseste implicit 127.0.0.1:11434; pentru llama.cpp se indica --url
cu adresa serverului local compatibil OpenAI, de exemplu http://127.0.0.1:8080.
Rezultatele noi se scriu separat, nu peste cele existente.

prompturi.jsonl contine cele 2.710 cereri aferente textelor AI evaluate:
2.590 din corpusul principal si 120 din experimentul suplimentar. Fiecare cerere
pastreaza modelul, promptul de sistem, promptul utilizatorului si optiunile.
modele_setari.json rezuma modelele si variantele de parametri; seed-ul si bugetul
de tokeni pentru fiecare cerere se gasesc in prompturi.jsonl.

In corpusul principal, Qwen2.5 a fost rulat de un coleg prin llama.cpp; celelalte
generari si experimentul suplimentar au folosit Ollama. Reluarea unei cereri nu
garanteaza un text identic intre versiuni de software, hardware sau cuantizari.

Referinte:
  https://unsloth.ai/docs/basics/train-your-own-decision-model-with-unsloth
  https://github.com/unslothai/notebooks
  Arhiva UNIMEDIA, articole din 2018 (provenienta presupus umana).

Componentele externe isi pastreaza licentele proprii. Textele generate pot contine
fictiune sau erori; rezultatele nu constituie o dovada universala a autoriei.
