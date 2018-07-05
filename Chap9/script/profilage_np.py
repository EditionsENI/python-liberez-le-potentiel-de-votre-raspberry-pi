import cProfile
import pstats
import io


if __name__ == '__main__':

    pr = cProfile.Profile()
    pr.enable()
    for j in range(1000):
        l = []
        for i in range(100):
            if i % 2 == 0:
                l.append(i)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
