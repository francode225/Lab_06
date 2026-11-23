LONGUEUR_MIN = 8

mot_de_passe = input("Entrez un mot de passe : ")

a_majuscule = False
a_minuscule = False
a_chiffre = False
a_special = False

for car in mot_de_passe:
    if car.isupper():
        a_majuscule = True
    elif car.islower():
        a_minuscule = True
    elif car.isdigit():
        a_chiffre = True
    elif not car.isspace():
        a_special = True

assez_long = len(mot_de_passe) >= LONGUEUR_MIN

criteres = [
    (assez_long,   f"Au moins {LONGUEUR_MIN} caractères"),
    (a_majuscule,  "Une lettre majuscule"),
    (a_minuscule,  "Une lettre minuscule"),
    (a_chiffre,    "Un chiffre"),
    (a_special,    "Un caractère spécial (!, @, #, $, %, etc.)"),
]

print("\nCritères du mot de passe :")
respectes = 0
for ok, description in criteres:
    if ok:
        print(f"  ✔ {description}")
        respectes += 1
    else:
        print(f"  x {description}")

print(f"\n{respectes} critère(s) sur {len(criteres)} respecté(s).")
if respectes == len(criteres):
    print("Mot de passe valide.")
else:
    print("Mot de passe trop faible.")