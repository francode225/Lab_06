mot = input("Entrez un mot : ").strip().lower()

if mot == "":
    print("Aucun mot saisi.")
elif mot == mot[::-1]:
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")