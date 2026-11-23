LONGUEUR_MIN = 5

nom = input("Entrez un nom d'utilisateur : ")

lettres_et_chiffres = nom.isalnum()
assez_long = len(nom) >= LONGUEUR_MIN

if lettres_et_chiffres and assez_long:
    print("Nom d'utilisateur valide.")
else:
    print("Nom d'utilisateur invalide :")
    if not lettres_et_chiffres:
        print("  - il doit contenir uniquement des lettres et des chiffres")
    if not assez_long:
        print(f"  - il doit contenir au moins {LONGUEUR_MIN} caractères")