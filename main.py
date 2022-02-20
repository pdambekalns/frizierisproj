import jaut   #Importē lietotāja definētu funkciju.

# Konsolē izvada salona nosaukumu un kādas darbības programma piedāvā.
print("VEIC PIERAKSTU SALONĀ 'PĒTERIS' ")
print("Ja nevēlaties izmantot programmu, lai pierakstītos zvaniet uz +371 24202469")
print("Izvēlies kādu no sekojošajiem!:")
print("A-Apskatīt visas rezervācijas")
print("B-Veikt pierakstu")
print("C-Dzēst rezervācijas")
print("E-Iziet")

# Piešķir mainīgajam lietotāja ievadīto vērtību un uztaisa to par lielo burtu.
izvele_darb= input('Ievadi izvēlēto burtu: ').upper()

# Izsauc funkciju, lai tā sāk darbību un izvada lietotāja prasīto konsolē.
jaut.funkcija(izvele_darb)

# Izveidojas fails "rezervacijas.txt", faila pirmajā rindā tiek ierakstīti nosaukumi, zem kuriem uzkrāsies attiecīgie dati.
while True:
  try:
    file = open("rezervacijas.txt", "r")
  except FileNotFoundError:
    file = open("rezervacijas.txt", "w")
    file.write("#\t\t\t\tVĀRDS UZVĀRDS\t\t\tDATUMS\t\t\tLAIKS\t\t\t\t\tT.NR.\t\t\t\tFRIZIERIS\n")
  file.close()


