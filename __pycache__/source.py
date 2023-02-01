import sys,pathlib,datetime,os
systemPath = str(pathlib.Path().resolve())
systemPath = str(pathlib.Path().resolve())
path = systemPath+"\__pycache__\logs.txt"
sys.stdout = open(path,"w")
def ran(x):
    for i in range(100):
        if i % 2 == 0:
            print('even')
        else:
            print('odd')
    return 0

print(ran(100))