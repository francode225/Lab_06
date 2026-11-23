PONCTUATION = ".,;:!?\"()"      # signes à retirer autour des mots

phrase = input("Entrez une phrase : ")
mots = phrase.split()

if len(mots) == 0:
    print("Aucun mot saisi.")
else:
    plus_long = mots[0].strip(PONCTUATION)
    for mot in mots[1:]:
        mot = mot.strip(PONCTUATION)
        if len(mot) > len(plus_long):
            plus_long = mot
    print(f"Mot le plus long : {plus_long}")