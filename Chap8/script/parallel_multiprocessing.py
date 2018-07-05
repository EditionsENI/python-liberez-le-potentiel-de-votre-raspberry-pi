import multiprocessing as mp
import random
import string

random.seed(123)

sortie = mp.Queue()


def chaine_aleatoire(taille, sortie):
    s_aleatoire = ''.join(random.choice(
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits)
                       for i in range(taille))
    sortie.put(s_aleatoire)


processes = [mp.Process(target=chaine_aleatoire, args=(5, sortie))
             for x in range(100)]

for p in processes:
    p.start()

for p in processes:
    p.join()

res = [sortie.get() for p in processes]

print(res)
