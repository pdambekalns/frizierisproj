def pulkst(m):  # izveido funkciju un piešķir tai vērtību.
  if m == "A": # Pārbauda vai "m" ir vienāds ar "A", ja vienāds tad izvada nākamās 5 rindās redzamo teksu.
    print("Izvēlies savu pieraksta laiku:")
    print("1-8.00-11.00")
    print("2-11.15-14.20")
    print("3-15.00-17.40")
    print("4-17.55-20.30")
    t = input("Izvēlies savu laiku:") # Piešķir mainīgajam, lietotāja izvēlēto skaitli.
    if t=="1": # Salīdzina skaitli ar zemāk redzmām vērtībām un kad tā sakrīt mainīgajam "l" piešķir attiecīgo laiku.
      l="8.00-11.00"
    elif t=="2":
      l="11.15-14.20"
    elif t=="3":
      l="14.35-17.40"
    elif t=="4":
      l="17.55-20.30"
    else:
      print("kļūda") # Ja neviens izvēlētais skaitlis nesakrīt konsolē izvada "kļūda"
  elif m == "B": # Pārbauda vai "m" ir vienāds ar "B", ja vienāds tad izvada nākamās 8 rindās redzamo teksu.
    print("Izvēlies savu pieraksta laiku:")
    print("1-9.00-10.00")
    print("2-10.30-11.50")
    print("3-12.40-13.40")
    print("4-14.00-15.00")
    print("5-15.20-16.20")
    print("6-16.40-17.40")
    print("7-18.00-19.00")
    t = input("Izvēlies savu laiku:") # Piešķir mainīgajam, lietotāja izvēlēto skaitli.
    if t=="1": # Salīdzina skaitli ar zemāk redzmām vērtībām un kad tā sakrīt mainīgajam "l" piešķir attiecīgo laiku.
      l="9.00-10.00"
    elif t=="2":
      l="10.30-11.50"
    elif t=="3":
      l="12.40-13.40"
    elif t=="4":
      l="14.00-15.00"
    elif t=="5":
      l="15.20-16.20"
    elif t=="6":
      l="16.40-17.40"
    elif t=="7":
      l="18.00-19.00"
    else:
      print("kļūda") # Ja neviens izvēlētais skaitlis nesakrīt konsolē izvada "kļūda"
  elif m == "C": # Pārbauda vai "m" ir vienāds ar "C", ja vienāds tad izvada nākamās 7 rindās redzamo teksu.
    print("Izvēlies savu pieraksta laiku:") 
    print("1-8.00-9.30")
    print("2-10.00-11.30")
    print("3-12.10-13.30")
    print("4-14.00-15.30")
    print("5-16.00-17.30")
    print("6-18.00-19.30")
    t = input("Izvēlies savu laiku:") # Piešķir mainīgajam, lietotāja izvēlēto skaitli.
    if t=="1": # Salīdzina skaitli ar zemāk redzmām vērtībām un kad tā sakrīt mainīgajam "l" piešķir attiecīgo laiku.
      l="8.00-9.30"
    elif t=="2":
      l="10.00-11.30"
    elif t=="3":
      l="12.10-13.30"
    elif t=="4":
      l="14.30-15.30"
    elif t=="5":
      l="16.00-17.30"
    elif t=="6":
      l="18.00-19.30"
    else:
      print("kļūda") # Ja neviens izvēlētais skaitlis nesakrīt konsolē izvada "kļūda"
  else:
    print("Izvēlies kādu no piedāvātajām opcijām!") # Izvada tekstu konsolē.
  return l # Kad izsauc funkciju, funkcija izvada vērtību l