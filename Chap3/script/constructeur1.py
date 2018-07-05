class Telephone(object):

    def __init__(self, val_modele, val_couleur, val_annee = 2002):
        self.marque = ""
        self.modele = val_modele
        self.couleur = val_couleur
        self.annee = val_annee


print("Instance t1 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t1 = Telephone("3310", "jaune", 1997)
# modification de l'attribut marque
t1.marque = "Nokia"
# Affichade de toutes les valeurs des attributs
print("Valeur pour l'attribut marque : ", t1.marque)
print("Valeur pour l'attribut modele : ", t1.modele)
print("Valeur pour l'attribut couleur : ", t1.couleur)
print("Valeur pour l'attribut annee : ", t1.annee)

print("\nInstance t2 avec annee par défaut")
# Instanciation de la classe en utilisant la valeur par défaut pour annee
t2 = Telephone("5510", "bleu")
# modification de l'attribut marque
t2.marque = "Nokia"
# Affichade de toutes les valeurs des attributs
print("Valeur pour l'attribut marque : ", t2.marque)
print("Valeur pour l'attribut modele : ", t2.modele)
print("Valeur pour l'attribut couleur : ", t2.couleur)
print("Valeur pour l'attribut annee : ", t2.annee)
