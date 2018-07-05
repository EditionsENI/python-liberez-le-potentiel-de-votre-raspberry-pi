from mes_fonctions import somme

val_a = 7
p, s = somme(val_a)
print("Valeur produit : ", p, " Valeur somme : ", s)

p, s = somme(val_a, c=3)
print("Valeur produit : ", p, " Valeur somme : ", s)

