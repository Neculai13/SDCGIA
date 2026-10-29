SDCGIA - Detectarea originii textelor de stiri in limba romana
Tema 6 - Studiu integrat: prima incercare, evaluare locala, corpus extins

Raportul urmareste ce s-a realizat efectiv, in ordine experimentala:
  1. v1: 6.357 texte, test intern 952/954 corecte (99,79%).
  2. Supliment Qwen: 120 AI + 30 controale, 150/150 corecte pe Colab.
  3. v1 inghetat pe CPU: 283/702 GPT detectate (recall 40,31%), 419 ratate;
     100/100 controale umane corecte. Acuratete mixta: 383/802 (47,76%).
  4. v3: adaptare noua pe 7.950 texte, test intern 1.199/1.199 corecte.

Scorul v3 nu demonstreaza rezolvarea generalizarii: corpusul si partitiile
s-au schimbat, GPT este reprezentat in antrenare, iar datele au fost deja
explorate. v3 nu reprezinta o evaluare externa neatinsa dupa dezvoltare.
Raportul explica limitele si include sase exemple originale comentate.

DE CITIT
  raport.pdf - raportul integrat actual, cu metode, tabele, exemple si limite
  raport_sursa.txt - acelasi continut, in format text editabil
  rezultate/exemple.json - fragmente, identificatori, hash-uri si predictii

COD SI DATE
  notebook.ipynb - fluxul istoric v1; datele si codul lui au ramas neschimbate
  notebook_v3.ipynb - fluxul v3 cu descarcare verificata din acest repository
  date/SDCGIA_human_ai_v1.zip - train/calibration/test v1: 4448/955/954
  date/supplementary_evaluation.zip - suplimentul Qwen deja generat
  date/SDCGIA_date_complete_v3.zip - v3: 5557/1194/1199 si provenienta
  date/evaluare_locala_v1_GPT.zip - cele 702 GPT si 100 controale; texte si
      cheie separata. Etichetele nu sunt trimise predictorului.
  generare/ - cereri si setari istorice v1; cod optional de generare locala
  generare/v3/ - inventarul extins de cereri si setari, inclusiv GPT
  rezultate/principal.json, sampling.json - rezultatele istorice v1
  rezultate/v1/ - configuratia, calibrarea si predictiile istorice v1 pe GPU
  rezultate/evaluare_locala_v1*.json* - evaluarea locala a modelului v1
  rezultate/v3/ - configuratia, calibrarea, predictiile si rezultatele v3

RULARE v1
  https://colab.research.google.com/github/Neculai13/SDCGIA/blob/main/notebook.ipynb
  Sesiune noua, Runtime > Change runtime type > T4 GPU, apoi Run all.
  Notebookul descarca datele deja generate, antreneaza de la zero un adaptor,
  calibreaza si evalueaza. Nu este necesara generarea locala a textelor.
  Rezultatele sunt in /content/SDCGIA/runs/ si experiment_colab.zip.
  /content este temporar: descarca arhiva inainte de pierderea sesiunii.

RULARE v3
  https://colab.research.google.com/github/Neculai13/SDCGIA/blob/main/notebook_v3.ipynb
  1. Selecteaza T4 GPU. RUN_MODE="prepare"; ruleaza sectiunile 1-5.
  2. Reporneste sesiunea; RUN_MODE="pilot"; ruleaza pana la sectiunea 7 inclusiv.
     Verifica pilot_complete.json si raportul backendului eficient.
  3. Reporneste sesiunea; RUN_MODE="train", CONFIRM_FULL_TRAINING=True;
     alege un RUN_NAME nou. Ruleaza pregatirea si antrenarea, apoi calibrarea.
  4. Activeaza RUN_FINAL_TEST=True pentru testul final; ruleaza arhivarea.
  Pentru reluare pastreaza RUN_NAME si indica RESUME_CHECKPOINT din acelasi run.
  Pentru calibrare/evaluare intr-o sesiune noua foloseste acelasi RUN_NAME si
  RUN_MODE="calibrate"/"evaluate", conform explicatiilor din notebook.
  Notebookul descarca singur datele in Drive si verifica hash-urile.
  Rezultatele se salveaza in MyDrive/SDCGIA/experiments/<RUN_NAME>/.

Greutatile modelului istoric nu sunt incluse in Git. Reluarea inferentei cu
exact adaptorul istoric necesita arhiva modelului, distribuita separat.
Notebookurile pot antrena un adaptor nou direct din datele publicate.
Nu pretindem o noua rulare GPU completa a notebookurilor dupa ambalare.
Versiunile principale sunt fixate, dar reproducerea bit cu bit nu e garantata.
Evita suprascrierea experimentelor istorice: foloseste un nume nou.

INTERPRETARE
  AI recall = TP/(TP+FN); FPR = FP/(FP+TN), calculat pe texte umane.
  Nu se aduna controalele umane reutilizate intre tabele per generator.
  Cele 120 texte Qwen au fost generate local, dar evaluate pe GPU Colab.
  Evaluarea celor 702 GPT a fost pe CPU local, cu modelul v1 calibrat inghetat.
  Numele GPT sunt etichete consemnate din interfata web, nu identificatori API
  certificati. Setarile numerice ale generarii web nu sunt disponibile.
  Qwen2.5 initial a fost generat prin llama.cpp; celelalte modele locale si
  suplimentul Qwen au folosit Ollama. Cerintele si abaterile sunt in raport.
