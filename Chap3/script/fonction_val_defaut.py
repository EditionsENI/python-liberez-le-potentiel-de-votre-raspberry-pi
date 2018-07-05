def somme(a, b=4, c=10):
    produit = a * b * c
    somme = a + b + c

    return produit, somme


val_a = 7
p, s = somme(val_a, c=3)
print("Valeur produit : ", p, " Valeur somme : ", s)


