import sys


def f_cas_1():
    print("Cas 1\n")


def f_cas_2():
    print("Cas 2\n")


def f_cas_3():
    print("Cas 3\n")


def f_cas_4():
    print("Cas 4\n")


def f_cas_s(chaine):
    print("Argument : ", chaine, " non reconnu \n")


def f_exit():
    sys.exit(1)


if len(sys.argv) < 2:
    print("aucune valeur passé en argument")
    f_exit()

val = sys.argv[1]

if int(val) == 1:
    f_cas_1()

elif int(val) == 2:
    f_cas_2()

elif int(val) == 3:
    f_cas_3()

elif int(val) == 4:
    f_cas_4()

else:
    f_cas_s()
    f_exit()
