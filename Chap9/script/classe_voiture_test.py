import unittest
from classe_voiture import Voiture


class VoitureTest (unittest.TestCase):

    def test_cons(self):

        ma_voiture = Voiture(modele='Mustang', marque='ford', annee='1968')
        self.assertEqual(ma_voiture.modele, 'Mustang')

    def test_augmente_carburant(self):

        ma_voiture = Voiture(modele='Mustang', marque='ford', annee='1968')
        ma_voiture.augmente_carburant()
        self.assertEqual(ma_voiture.vol_carburant, 2)


if __name__ == '__main__':
    unittest.main()
