import laiks
import cenas
from datetime import datetime
dienas=[]
def funkcija(izvele):
    if izvele == "A":
      skaits=0
      file = open("rezervacijas.txt")
      lines = file.readlines()[1:]
      file.close()
      for line in lines:
          skaits += 1

      if skaits == 0:
          print("Nav neviena pieraksta!!")
          print()
      else:
          file = open("rezervacijas.txt", "r")
          print(file.read())
          file.close()  


    elif izvele == "B":
      with open("rezervacijas.txt", "r") as file:
          for pedeja_l in file:
            pass
          if pedeja_l[0] == "#":
            numurs = 1
          else:
            numurs = int(pedeja_l[0]) + 1
      vards = input("Ievadi vārdu un uzvārdu: ")
      print()
      datums = input("Ievadi datumu (ievadi-gadu.mēnesi.dienu-(Pimēram:2022.02.16)): ")
      print()
      dienas=datums.split(".")
      #print(dienas)
      for i in range(0, len(dienas)):
          dienas[i] = int(dienas[i])
      if dienas[0]<2021:
        print("Ievadi pareizu datumu!")
      elif dienas[1]<0 and dienas[1]>12:
        print("Ievadi pareizu datumu!")
      elif dienas[2]<0 and dienas[2]>31:
        print("Ievadi pareizu datumu!")
      else:
        year=dienas[0]
        month=dienas[1]
        day=dienas[2]
        d=datetime(year,month,day)
        if d.weekday()>4:
          print("Šī ir brīvdiena, izvēlieties citu datumu.")
        else:
            print("Pieejamie frizieri:")
            print("Katra friziera specialitāte:")
            print("ALAIŽA - Matu krāsošana,balināšana, apgriešana un ieveidošana.")
            print("SENCIS - Apgriež vīriešiem matus un ieveido.")
            print("PĒTERIS - matu kopšana un ieveidošana.")
            print()
            print("A-Alaiža\tB-Andris\tC-Pēteris")
            frizieris =input("Izvēlies frizierim attiecīgo burtu: ").upper()
            print()
            p_laiks= laiks.pulkst(frizieris)
            print()
            t_nr =input("Ievadi talruņa nr.: ")
            print()
            cena= cenas.samaksa(frizieris)
            print()
            if frizieris=="A":
              frizieris1="Alaiža"
            elif frizieris=="B":
              frizieris="Sencis"
            else:
              frizieris1="Pēteris"
              file=open("rezervacijas.txt","a")                
              file.write(f"{numurs}\t\t\t{vards}\t\t\t{datums}\t\t\t{p_laiks}\t\t\t{t_nr}\t\t\t{frizieris1}\n") 
              file.close()
              print("Pieraksts ir veikts! :)")
                

    elif izvele == "C":
        numurs = input("Ievadi pieraksta numuru: ")
        file1 = open("rezervacijas.txt", "r")
        linijas = file1.readlines()
        file1.close()
        file2 = open("rezervacijas.txt", "w")

        for line in linijas:
            if not line.startswith(numurs):
                file2.write(line)
            file2.close()

    elif izvele == "E":
        print("Uzredzēšanos!")

    else:
        print("Nepareiza atbilde. Mēģiņat vēlreiz.")