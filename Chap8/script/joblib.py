import random
import string

from joblib import Parallel, delayed

random.seed(123)


def chaine_aleatoire(taille):
    rand_str = ''.join(random.choice(
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits)
                       for i in range(taille))
    return rand_str


res = Parallel(n_jobs=4)(delayed(chaine_aleatoire)(5)
                             for _ in range(100))

print(res)

