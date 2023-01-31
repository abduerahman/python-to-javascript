import sys,pathlib,datetime,os
systemPath = str(pathlib.Path().resolve())
systemPath = str(pathlib.Path().resolve())
path = systemPath+"\__pycache__\logs.txt"
sys.stdout = open(path,"w")


print('Hello,World')

arra = [1,2,3,4]

for i in range(4):
    print(arra[i])

def hello(x):
    y = 10
    x = 20
    return 'hello,World'

x = hello('hello')
print(x)