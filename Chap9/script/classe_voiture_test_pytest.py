from classe_voiture import Voiture


def test_cons():

    ma_voiture = Voiture(modele='Mustang', marque='ford', annee='1968')
    assert ma_voiture.modele == 'Mustang'
    assert type(ma_voiture.modele) is str
    assert type(ma_voiture.marque) is str
    assert type(ma_voiture.marque) is int or float


def test_augmente_carburant():

    ma_voiture = Voiture(modele='Mustang', marque='ford', annee='1968')
    ma_voiture.augmente_carburant()
    assert ma_voiture.vol_carburant == 1
