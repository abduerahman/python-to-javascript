import sys,pathlib,datetime,os
systemPath = str(pathlib.Path().resolve())
systemPath = str(pathlib.Path().resolve())
path = systemPath+"\__pycache__\logs.txt"
sys.stdout = open(path,"w")
def hello(x):
    y = 10
    return y

y = hello(10)