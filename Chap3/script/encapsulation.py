class Telephone(object):

    def __init__(self, val_modele, val_couleur, val_annee = 2002):
        self._marque = ""
        self._modele = val_modele
        self._couleur = val_couleur
        self._annee = val_annee

    def aff_attribut(self):
        print("Valeur pour l'attribut marque : ", self._marque)
        print("Valeur pour l'attribut modele : ", self._modele)
        print("Valeur pour l'attribut couleur : ", self._couleur)
        print("Valeur pour l'attribut annee : ", self._annee)

    def calc_cote(self, annee_en_cours, valeur_achat, serie_spec = False):

        bonus = 0
        nb_annee = annee_en_cours - self._annee
        if nb_annee < 10:
            decote = 0.1 * nb_annee
        else:
            decote = 0.9

        if serie_spec == True:
            bonus = 0.1 * valeur_achat

        valeur = valeur_achat - (valeur_achat * decote) + bonus

        return valeur

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, value):
        self._marque = value

    @property
    def modele(self):
        return self._modele

    @modele.setter
    def modele(self, value):
        self._modele = value

    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self, value):
        self._couleur = value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, value):
        self._annee = value

print("Instance t1 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t1 = Telephone("3310", "jaune", 1997)
# modification de l'attribut marque
t1.marque = "Nokia"
# Affichade de toutes les valeurs des attributs
print("La marque de t1 est : ", t1.marque)



