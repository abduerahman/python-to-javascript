import sys,pathlib,datetime,os

filePath = sys.argv[1]
outFile = sys.argv[2]
systemPath = str(pathlib.Path().resolve())

text = 'import sys,pathlib,datetime,os\nsystemPath = str(pathlib.Path().resolve())\nsystemPath = str(pathlib.Path().resolve())\npath = systemPath+"\__pycache__\logs.txt"\nsys.stdout = open(path,"w")\n'

file = open('D:\python-to-javascript-conventer\__pycache__\source.py','w')
file.write(text)

sourceFile = open(filePath,'r')

for i in sourceFile.readlines():
    file.writelines(i)

file.close()

filePath = 'D:\python-to-javascript-conventer\__pycache__\source.py'

try:
   ex = os.system('py {path}'.format(path = filePath))
   if(ex == 0):
    os.system('py {path} {inputFile} {outFile}'.format(path = systemPath+'\index.py', inputFile = filePath, outFile = outFile))
except TypeError:
    logsFile = open(systemPath+'\__pycache__\logs.txt','a')
    logsFile.write(str(TypeError)+' '+str(datetime.date().today())+'\n')
    logsFile.close()