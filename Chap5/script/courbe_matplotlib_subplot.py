import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("../data/titanic.csv")
    l_age = df['age']
    l_age_m = l_age[:]
    l_age_m *= 0.9

    plt.figure(0)

    plt.title("Age des passarges du titanic")

    plt.subplot(211)
    plt.plot(l_age_m, label="liste des ages * 0.9")
    plt.legend()

    plt.subplot(212)
    plt.plot(l_age, label="listes des ages")

    plt.xlabel("Numéro d'echantillons")
    plt.ylabel("Age (années)")

    plt.legend()
    plt.show()
