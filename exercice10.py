CHIFFRES_VISIBLES = 4

numero = input("Entrez votre numéro de carte de crédit : ")

if len(numero) <= CHIFFRES_VISIBLES:
    print("Numéro trop court pour être masqué.")
else:
    masque = "*" * (len(numero) - CHIFFRES_VISIBLES) + numero[-CHIFFRES_VISIBLES:]
    print(f"Numéro masqué : {masque}")