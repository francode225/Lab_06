texte = input("Entrez une chaîne de caractères : ")

lettres = 0
chiffres = 0
espaces = 0
for car in texte:
    if car.isalpha():
        lettres += 1
    elif car.isdigit():
        chiffres += 1
    elif car.isspace():
        espaces += 1

print(f"Lettres : {lettres}")
print(f"Chiffres : {chiffres}")
print(f"Espaces : {espaces}")