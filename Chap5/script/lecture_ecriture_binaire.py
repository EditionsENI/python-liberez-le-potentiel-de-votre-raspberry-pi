from struct import pack
from struct import unpack
from random import randint

with open('test_ecriture.bin', 'wb') as mon_fichier:
    print('ouverture et création fichier en mode binaire :  OK!')
    for i in range(10):
        val = randint(0, 100)
        mon_fichier.write(pack(">I", val))
        print("Valeur numérique ajoutée au fichier : " + str(val))

with open('test_ecriture.bin', 'rb') as mon_fichier:
    print('ouverture fichier en mode binaire :  OK!')
    for i in range(10):
        val = mon_fichier.read(4)
        val_int = unpack(">i", val)
        print("Valeur numérique ajoutée au fichier : " + str(val_int[0]))
