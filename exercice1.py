VOYELLES = "aeiouy"

mot = input("Entrez un mot : ")

compteur = 0
for lettre in mot.lower():
    if lettre in VOYELLES:
        compteur += 1

s = "s" if compteur > 1 else ""
print(f"Le mot contiet {compteur} voyelle{s}.")