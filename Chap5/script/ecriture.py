from random import randint

with open('test_ecriture.txt', 'w') as mon_fichier:
    print('ouverture et création fichier OK!')
    chaine_ecrire = "Senatus populusque romanus\n"
    mon_fichier.write(chaine_ecrire)
    print("Écriture dans le fichier de la chaine : ", chaine_ecrire)

    for i in range(10):
        val = randint(0, 100)
        mon_fichier.write(str(val)+'\n')
        print("Valeur numérique ajoutée au fichier : " + str(val))
    mon_fichier.close()
