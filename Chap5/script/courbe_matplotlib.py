import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("../data/titanic.csv")
    l_age = df['age']
    l_age_m = l_age[:]
    l_age_m *= 0.9

    plt.figure(0)
    plt.plot(l_age_m, label="liste des ages * 0.9")

    plt.xlabel("Numéro d'echantillons")
    plt.ylabel("Age (années)")

    plt.title("Age des passagers du titanic * 0.9")

    plt.legend()

    plt.figure(1)

    plt.plot(l_age, label="listes des ages")
    plt.xlabel("Numéro d'echantillons")
    plt.ylabel("Age (années)")

    plt.title("Age des passagers du titanic")

    plt.legend()
    plt.show()
