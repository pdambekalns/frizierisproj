import laiks #Iportē lietotāja definētu funkciju.
import cenas #Iportē lietotāja definētu funkciju.
from datetime import datetime # Importē datumus un laikus no funkcijas "datetime".
dienas=[] # Izveido tikšu listu.
numurs=0 # Piešķir mainīgajam vērtību 0.
def funkcija(izvele): # izveido funkciju un piešķir tai vērtību.
    if izvele == "A": # Pārbauda vai "izvele" ir vienādā ar "A", ja ir tad zemākās darbības izvadīs konsolē, to ko lietotājs ir izvēlējies.
      skaits=0 # Piešķir mainīgajam vērtību 0.
      file = open("rezervacijas.txt") # Atver failu.
      lines = file.readlines()[1:] # Nolasa visas līnijas failā.
      file.close() # Aizveras fails.
      for line in lines: # Nolasa līniju skaitu.
          skaits += 1 #pievieno mainīgajam vērtību attiecībā uz līniju skaitu.

      if skaits == 0: # Pārbauda vai līniju skaits ir 0, ja nulle tad izvada teksu kas ir redzams zemāk.
          print("Nav neviena pieraksta!!") 
          print() 
      else: # Parbauda vai līniju skaits nav nulle, ja nav tad nolasa un izvada tekstu un no faila nolasītās līnijas.
          file = open("rezervacijas.txt", "r")
          print("Apskati jau rzervētos laikus un veic pierakstu sev izvedīgā laikā.")
          print(file.read())
          file.close()  # Aizver failu.


    elif izvele == "B": # Pārbauda vai "izvele" ir vienādā ar "B", ja ir tad zemākās darbības izvadīs konsolē, to ko lietotājs ir izvēlējies.
      with open("rezervacijas.txt", "r") as file: # fails tiek atvērts. Rindas zemāk pārbauda rezervacijas numuru, ja failā nolasītā rinda sakrīt ar simbolu "#", tad nakamai rindai piešķir nākamo numuru.
          for pedeja_l in file:
            pass
      if pedeja_l[0] == "#":
          numurs = 1
      else: # 
              numurs = int(pedeja_l[0]) + 1
      # Kad rindai piešķirts numur sāk konsolē uzdot jautājumus, lai lietotājs ievada vārdu, uzvārdu un datumu.
      vards = input("Ievadi vārdu un uzvārdu: ")
      print()
      datums = input("Ievadi datumu (ievadi-gadu.mēnesi.dienu-(Pimēram:2022.02.16)): ")
      print()
      dienas=datums.split(".") # datumu sadala un ieliek list kā trīs dažādus mainīgos.
      #print(dienas)
      for i in range(0, len(dienas)): # Pārbauda vai datums ir reāls. Ja nav tadizvada "Ievadi pareizu datumu!"
          dienas[i] = int(dienas[i])
      if dienas[0]<2021:
        print("Ievadi pareizu datumu!")
      elif dienas[1]<0 and dienas[1]>12:
        print("Ievadi pareizu datumu!")
      elif dienas[2]<0 and dienas[2]>31:
        print("Ievadi pareizu datumu!")
      else: # Ja datums ir reāls tad zemāk pārbauda vai tā ir brīvdiena.
        year=dienas[0] 
        month=dienas[1]
        day=dienas[2]
        d=datetime(year,month,day) # Ar importēto datetime, pārbauda vai datums ir brīvdiena.
        if d.weekday()>4:
          print("Šī ir brīvdiena, izvēlieties citu datumu.") # Ja brīvdiena tad izvada šo tekstu.
        else: # Ja datums nav brīvdiena, tad tiek izvadīts teksts un jautājumi zemāk.
            print("Pieejamie frizieri:")
            print("Katra friziera specialitāte:")
            print("ALAIŽA - Matu krāsošana,balināšana, apgriešana un ieveidošana.")
            print("SENCIS - Apgriež vīriešiem matus un ieveido.")
            print("PĒTERIS - matu kopšana un ieveidošana.")
            print()
            print("A-Alaiža\tB-Andris\tC-Pēteris")
            frizieris =input("Izvēlies frizierim attiecīgo burtu: ").upper() # Piešķir mainīgajam lietotāja ievadīto burtu un uztaisa to par lielo burtu.
            print() 
            p_laiks= laiks.pulkst(frizieris)
            print() # Izsauc impoerteto funkciju, piešķir mainīgajam lietotāja ievadīto vērtību.
            t_nr =input("Ievadi talruņa nr.: ") # Piešķir mainīgajam lietotāja ievadīto atbildi uz jautājumu.
            print() 
            cena= cenas.samaksa(frizieris) # Izsauc impoerteto funkciju, piešķir mainīgajam lietotāja ievadīto vērtību.
            print()
            if frizieris=="A": # Šeit pārbauda lietotāja atbildi un piešķir mainīgajam attiecīgo vārdu, ko ievadīt failā pie datu uzglabāšanas, lai vieglāk pārskatīt.
              frizieris1="Alaiža"
            elif frizieris=="B":
              frizieris1="Sencis"
            else:
              frizieris1="Pēteris"

            file=open("rezervacijas.txt","a")    # Atver failu.
            file.write(f"{numurs}\t\t\t{vards}\t\t\t{datums}\t\t\t{p_laiks}\t\t\t{t_nr}\t\t\t{frizieris1}\n")  # Ievada rindā katru attiecīgo vērtību.
            file.close() # Aizver failu.
            print(f"Pieraksts ir veikts, gaidīsim jūs {datums} plkst. {p_laiks}! :)") # Izvada pieraksta apstiprinājumu, pieraksta datumu un laiku.
                

    elif izvele == "C": # Pārbauda vai "izvele" ir vienādā ar "C", ja ir tad zemākās darbības izvadīs konsolē, to ko lietotājs ir izvēlējies.
        numurs = input("Ievadi pieraksta numuru: ") # Izvada jautājumu konsolē.
        file1 = open("rezervacijas.txt", "r") # Atver failu.
        linijas = file1.readlines() # Piešķir mainīgajam no faila nolasīto līniju.
        file1.close() # Failu aizver.
        file2 = open("rezervacijas.txt", "w") # Failu Atver, lai pierakstītu informaciju.

        for line in linijas: # Izdzēš līniju, kuras numur sakrīt ar lietotāja ievadīto.
            if not line.startswith(numurs):
                file2.write(line)
            file2.close()

    elif izvele == "E": # Pārbauda vai "izvele" ir vienādā ar "B", ja ir tad koncolē izvada "Uzredzēšanos!"
        print("Uzredzēšanos!")

    else: #Lietotāja ievadītā atbilde nesakrīt ar nevienu no koncolē piedāvātajām izvēlēm.
        print("Nepareiza atbilde. Mēģiņat vēlreiz.")
