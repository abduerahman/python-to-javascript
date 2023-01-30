import sys,pathlib,datetime,os
systemPath = str(pathlib.Path().resolve())
systemPath = str(pathlib.Path().resolve())
path = systemPath+"\__pycache__\logs.txt"
sys.stdout = open(path,"w")

for i in range(100):
    print(i)