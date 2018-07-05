import random
import time
from threading import Thread


def worker(i):
    temps = random.randrange(5)
    print("Le thread {} dormira {} sec".format(i, temps))
    time.sleep(temps)
    print("Le thread {} a fini de dormir".format(i))


for i in range(10):
    t = Thread(target=worker, args=(i,))
    t.start()

