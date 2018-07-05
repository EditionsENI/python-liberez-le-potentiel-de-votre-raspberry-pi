class Telephone(object):

    def __init__(self, val_modele, val_couleur, val_valeur = 750,
                 val_annee = 2002):
        self._marque = ""
        self._modele = val_modele
        self._couleur = val_couleur
        self._annee = val_annee
        self._valeur = val_valeur

    def __repr__(self):
        return "Année : " + str(self.annee) + " Marque : " + self.marque +\
            " Modele : " + self.modele + " Couleur : " + self.couleuri +\
            "Valeur : " + str(self.valeur)

    def __str__(self):
        return "Valeur pour l'attribut marque : " + self._marque + \
            "\nValeur pour l'attribut modele : " + self._modele +\
            "\nValeur pour l'attribut couleur : " + self._couleur +\
            "\nValeur pour l'attribut valeur : " + self._valeur +\
            "\nValeur pour l'attribut annee : " + str(self._annee)


    def __add__(self, objet_add):
        val_tot = self._valeur + objet_add.valeur
        return val_tot

    def aff_attribut(self):
        print("Valeur pour l'attribut marque : ", self._marque)
        print("Valeur pour l'attribut modele : ", self._modele)
        print("Valeur pour l'attribut couleur : ", self._couleur)
        print("Valeur pour l'attribut annee : ", self._valeur)
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

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, value):
        self._valeur = value

print("Instance t1 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t1 = Telephone("3310", "jaune", 35, 1997)

print("Instance t2 avec tous les arguments")
# Instanciation de la classe en précisannt tous les paramètres
t2 = Telephone("3310", "carbone", 45, 200)

# utilisation de l'oérateur + rédéfini pour la classe Telephone
val_cumul = t1 + t2
print("Valeur cumulée des deux téléphone : ", val_cumul)



