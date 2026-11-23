courriel = input("Entrez une adresse courriel : ").strip()

position_arobase = courriel.find("@")
if position_arobase == -1:
    print("Adresse invalide : il manque le caractère @.")
else:
    apres_arobase = courriel[position_arobase + 1:]

    if apres_arobase.find(".") == -1:
        print("Adresse invalide : il manque un point après le @.")
    else:
        print("L'adresse est valide.")