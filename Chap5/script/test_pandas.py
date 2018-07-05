import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("../data/titanic.csv")
    df.index
    df.columns
    df.dtypes
    l_age = df['age']
    age_moyen = l_age.mean()
    age_std = l_age.std()

    # histogramme_age = l_age.hist()
    print("Age moyenne des passagers : ", age_moyen)
    print("Ecart-type de l'age des passagers : ", age_std)

    l_age_sup50 = df[df['age'] > 50]

    print("Nombre de passagers ayant plus de 50 ans : ", len(l_age_sup50))
