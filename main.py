import sys,pathlib,datetime,os

filePath = sys.argv[1]
outFile = sys.argv[2]
systemPath = str(pathlib.Path().resolve())

try:
   ex = os.system('py {path}'.format(path = filePath))
   if(ex == 0):
    os.system('py {path} {inputFile} {outFile}'.format(path = systemPath+'\index.py', inputFile = filePath, outFile = outFile))
except TypeError:
    logsFile = open(systemPath+'\__pycache__\logs.h','a')
    logsFile.write(str(TypeError)+' '+str(datetime.date().today())+'\n')
    logsFile.close()