NB_CHIFFRES = 16
CHIFFRES_VISIBLES = 4

saisie = input("Entrez votre numéro de carte de crédit : ")
numero = saisie.replace(" ", "").replace("-", "")

if numero == "":
    print("Erreur : aucun numéro saisi.")
elif not numero.isdigit():
    print("Erreur : le numéro ne doit contenir que des chiffres "
          "(peut avoit des espaces et les tirets).")
elif len(numero) < NB_CHIFFRES:
    print(f"Erreur : le numéro contient {len(numero)} chiffres, "
          f"il en manque {NB_CHIFFRES - len(numero)} (16 attendus).")
elif len(numero) > NB_CHIFFRES:
    print(f"Erreur : le numéro contient {len(numero)} chiffres, "
          f"soit {len(numero) - NB_CHIFFRES} de trop (16 attendus).")
else:
    masque = "*" * (NB_CHIFFRES - CHIFFRES_VISIBLES) + numero[-CHIFFRES_VISIBLES:]
    print(f"Numéro masqué : {masque}")