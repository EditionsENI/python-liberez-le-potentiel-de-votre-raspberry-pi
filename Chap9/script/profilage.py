import cProfile
import pstats
import io

from classe_voiture import Voiture


if __name__ == '__main__':

    pr = cProfile.Profile()
    pr.enable()
    for i in range(1000):
        ma_voitune = Voiture(marque='VW', modele='polo', annee=2018)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
