with open('fichier_a_lire.txt', 'r') as mon_fichier:
    print('ouverture fichier OK!')
    chaine_lue = mon_fichier.readline()
    print("Chaine lue : ", chaine_lue)

    while True:
        val_str = mon_fichier.readline()
        if not val_str:
            break
        val_int = int(val_str)

        print("Entier lu : ", str(val_int))
    mon_fichier.close()
