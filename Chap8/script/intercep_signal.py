import sys
import signal
import time


def reaction_intercept(signal, frame):
    print("Message intercepté \n")
    print("Le script sera fermé dans 5 sec\n")
    time.sleep(5)
    print("Fermeture")
    sys.exit(0)


# signal.signal(signal.SIGINT, reaction_intercept)


print("Le programme tourne en boucle en attendant la fermeture")
while True:
    continue
