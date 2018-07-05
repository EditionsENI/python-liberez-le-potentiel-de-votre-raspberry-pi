import os


if __name__ == '__main__':

    commande = "ls -la"
    res_commande = os.popen(commande)
    print("Résultats retournés par la commande : ", commande)
    print(res_commande.read())
