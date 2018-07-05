import csv
with open('../data/titanic.csv', 'r') as fichier_csv:
    data_titanic = csv.reader(fichier_csv, delimiter=',')
    for i, ligne in enumerate(data_titanic):
        if i == 0:
            premiere_ligne = ligne
        val_aff = ''
        for val in ligne:
            val_aff += (val + ',')
        print(val_aff)

with open('../data/titanic_edit.csv', 'w') as fichier_csv:
    data_edit = csv.writer(fichier_csv, delimiter=',')
    nouvelle_ligne = [0, 3, "male", 32.0, 0, 0, 7.75,
                      "Q", "Third", "man", "False", "",
                      "Queenstown", "no", "False"]

    data_edit.writerow(premiere_ligne)
    data_edit.writerow(nouvelle_ligne)
