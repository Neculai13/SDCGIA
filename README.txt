SDCGIA - Detectarea textelor umane si generate de AI
Tema 6: Decision model cu Unsloth

Continut:
  notebook.ipynb - notebookul adaptat, cu rezultatele din Colab
  generare/ - codul de generare, modelele, prompturile si setarile folosite
  rezultate/ - rezultate globale si per model-sursa, pentru cele doua experimente
  raport.pdf - descrierea implementarii, rezultatele si limitele
  date/SDCGIA_human_ai_v1.zip - datele de antrenare, calibrare si test

Detector: Unsloth Qwen3.5-4B, ajustat cu LoRA, antrenat si evaluat in Colab pe T4.
Corpus: 3.767 texte human si 2.590 texte AI.
Test principal: 952/954 clasificari corecte (99,79%), cu 1 FP si 1 FN.
Test suplimentar: 150/150 corecte, pe 30 surse noi, cu doua modele si doua
profiluri de sampling. Acest rezultat se raporteaza separat de testul principal.

Notebookul pastreaza rezultatele exportate din Colab; au fost omise celulele
temporare de diagnostic. Nu reprezinta o noua rulare integrala a experimentului.
Pentru rerulare este necesar un GPU in Colab. Datele sunt incluse in arhiva
date/SDCGIA_human_ai_v1.zip (4,35 MiB). Modelul salvat nu este inclus.

Date pentru Colab:
  1. Descarca date/SDCGIA_human_ai_v1.zip din repository.
  2. Incarca arhiva in Google Drive, in MyDrive/SDCGIA/colab/.
  3. In notebook, BUNDLE_PATH trebuie sa fie:
     /content/drive/MyDrive/SDCGIA/colab/SDCGIA_human_ai_v1.zip
  4. Nu dezarhiva manual: notebookul verifica si extrage bundle-ul.
Arhiva contine textele in formatul modelului si metadatele pentru cele trei
partitii: train 4.448, calibration 955, test 954. Numele v1 al bundle-ului este
cel folosit si de notebookul adaptat; nu indica un alt corpus.
Articolele integrale din arhiva isi pastreaza drepturile surselor originale.

Generare locala (Python 3.12; modelele trebuie instalate separat):
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
