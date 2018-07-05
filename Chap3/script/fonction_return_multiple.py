# Déclaration de la fonction
def somme_produit(a, b):
    p = a * b
    s = a + b

    return p, s


val_a = 2
val_b = 5
produit, somme = somme_produit(val_a, val_b)
print("Valeur produit : ", produit, " Valeur somme : ", somme)
