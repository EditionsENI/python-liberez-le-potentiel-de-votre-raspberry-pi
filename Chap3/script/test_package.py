from package_tel.telephonie import Telephone
from package_tel.telephonie import Smartphone


print("Instance t1 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t1 = Telephone("3310", "jaune", 35, 1997)

print("Instance t2 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t2 = Telephone("3310", "carbone", 45, 200)

# utilisation de l'oérateur + rédéfini pour la classe Telephone
val_cumul = t1 + t2
print("Valeur cumulée des deux téléphone : ", val_cumul)
print("Instance sp  de la Smartphone dérivée de la classe Telephone")

# Instanciation de la classe en précisannt tous les paramètres
sp = Smartphone("6820", "Gris", "Symbian", 300, 2005)

print("Modification de l'attribut marque")
sp.marque = "Nokia"

print("Marque de l'instance : ", sp.marque)
print("Os du l'instance : ", sp.os)
