class Telephone(object):

    def __init__(self, val_modele, val_couleur, val_annee = 2002):
        self.marque = ""
        self.modele = val_modele
        self.couleur = val_couleur
        self.annee = val_annee

    def aff_attribut(self):
        print("Valeur pour l'attribut marque : ", self.marque)
        print("Valeur pour l'attribut modele : ", self.modele)
        print("Valeur pour l'attribut couleur : ", self.couleur)
        print("Valeur pour l'attribut annee : ", self.annee)

    def calc_cote(self, annee_en_cours, valeur_achat, serie_spec = False):

        bonus = 0
        nb_annee = annee_en_cours - self.annee
        if nb_annee < 10:
            decote = 0.1 * nb_annee
        else:
            decote = 0.9

        if serie_spec == True:
            bonus = 0.1 * valeur_achat

        valeur = valeur_achat - (valeur_achat * decote) + bonus

        return valeur



print("Instance t1 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t1 = Telephone("3310", "jaune", 1997)
# modification de l'attribut marque
t1.marque = "Nokia"
# Affichade de toutes les valeurs des attributs
t1.aff_attribut()


print("\nInstance t2 avec annee par défaut")
# Instanciation de la classe en utilisant la valeur par défaut pour annee
t2 = Telephone("5510", "bleu")
# modification de l'attribut marque
t2.marque = "Nokia"
# Affichade de toutes les valeurs des attributs
t2.aff_attribut()

# calcul des cotes poéur t1 et t2
val_t1 = t1.calc_cote(2017, 35)
val_t2 = t2.calc_cote(2017, 35, True)

# affichage de la cote calculée
print("\n")
print("Valeur code t1 : ", val_t1)
print("Valeur code t2 : ", val_t2)

