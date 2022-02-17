def pulkst(m):
  if m == "A":
    print("Izvēlies savu pieraksta laiku:")
    print("1-8.00-11.00")
    print("2-11.15-14.20")
    print("3-15.00-17.40")
    print("4-17.55-20.30")
    t = input("Izvēlies savu laiku:")
    if t=="1":
      x="8.00-11.00"
    elif t=="2":
      x="11.15-14.20"
    elif t=="3":
      x="14.35-17.40"
    elif t=="4":
      x="17.55-20.30"
    else:
      print("kļūda")
  elif m == "B":
    print("Izvēlies savu pieraksta laiku:")
    print("1-9.00-10.00")
    print("2-10.30-11.50")
    print("3-12.40-13.40")
    print("4-14.00-15.00")
    print("5-15.20-16.20")
    print("6-16.40-17.40")
    print("7-18.00-19.00")
    t = input("Izvēlies savu laiku:")
    if t=="1":
      x="9.00-10.00"
    elif t=="2":
      x="10.30-11.50"
    elif t=="3":
      x="12.40-13.40"
    elif t=="4":
      x="14.00-15.00"
    elif t=="5":
      x="15.20-16.20"
    elif t=="6":
      x="16.40-17.40"
    elif t=="7":
      x="18.00-19.00"
    else:
      print("kļūda")
  elif m == "C":
    print("Izvēlies savu pieraksta laiku:")
    print("1-8.00-9.30")
    print("2-10.00-11.30")
    print("3-12.10-13.30")
    print("4-14.00-15.30")
    print("5-16.00-17.30")
    print("6-18.00-19.30")
    t = input("Izvēlies savu laiku:")
    if t=="1":
      x="8.00-9.30"
    elif t=="2":
      x="10.00-11.30"
    elif t=="3":
      x="12.10-13.30"
    elif t=="4":
      x="14.30-15.30"
    elif t=="5":
      x="16.00-17.30"
    elif t=="6":
      x="18.00-19.30"
    else:
      print("kļūda")
  else:
    print("Izvēlies kādu no piedāvātajām opcijām!")
  return x