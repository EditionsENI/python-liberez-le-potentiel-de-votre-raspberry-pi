import os


for dirpath, dirnames, filenames in os.walk(os.curdir):
    for fp in filenames:
        print(os.path.abspath(fp))
