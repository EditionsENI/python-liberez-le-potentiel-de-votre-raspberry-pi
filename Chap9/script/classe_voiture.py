class Voiture(object):

    def __init__(self, modele, marque, annee):
        """constructeur de la classe voiture

        paramètres :
            modele -- modèle de la voiture
            marque -- marque du véhicule
            annee -- année de fabrication
        """
        self.modele = modele
        self.marque = marque
        self.annee = annee
        self.vol_carburant = 0
        self.valeur = 0

    def augmente_carburant(self):
        """augmente le volume de carburant d'un litre"""
        self.vol_carburant += 1

    def reservoir_plien(self):
        """vérifie si le niveau de carburant est à 50L

        return : bolléen -- True si la valeur est 50 False sinon
        """
        if self.augmente_carburant == 50:
            return True
        else:
            return False

    def maj_val(self, nouv_val=10000):
        """Mise à jour de la valeur de la voiture en Euros

        paramètre :
            nouv_val -- valeur pour la mise à jour (10 000 par défaut)

        return :  entier -- valeur de l'attribut valeur après mise à jour
        """
        # -*- coding: utf-8 -*-
        self.valeur = nouv_val
        return self.valeur


if __name__ == '__main__':
        ma_voiture = Voiture(modele='406', marque='peugeot', annee=2014)
        ma_voiture.augmente_carburant()
