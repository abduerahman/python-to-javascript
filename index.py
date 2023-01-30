from keyWords import keyWords
from function import convertingForloop,removingIndentation
import function,datetime,pathlib,sys

dirPath = pathlib.Path().resolve()

inputFile = sys.argv[1]
outFileName = sys.argv[2]

file = open(inputFile,'r')
out = open(outFileName+'.js','w')

global_indentation = []
global_varible = []

prev = 0

for line in file.readlines():
    if len(line.strip()) > 0:
        currentIndetation = removingIndentation(line)
        
        if currentIndetation > prev:
            global_indentation.append(currentIndetation)
        
        if currentIndetation < prev and prev- currentIndetation > 1:
    
            if len(global_indentation) == 0:
                global_indentation.append(0)
            global_indentation.pop()
            if(len(global_indentation) == 0):
                global_indentation.append(0)
                
            praketIndentation = global_indentation.pop()
            out.writelines(function.makingIndenation(praketIndentation - 1))
            
        if (line.count('for ')) > 0 and line.count('range(') > 0:
            line = ' '* (currentIndetation -1) + convertingForloop(line)+'\n'
            
        if(function.varibleDeclration(line,currentIndetation) != None):
            varible = function.varibleDeclration(line,currentIndetation)
            v = [varible[1],varible[2]]
            if( v not in global_varible):
                global_varible.append(v)
                line = varible[0]+'\n'
        else:
            for keyWord in keyWords:
                if keyWord == 'def ' and line.count(keyWord) > 0:
                    global_varible = function.gettingParmater(line,global_varible,currentIndetation)
                if(line.count(keyWord) > 0):
                    line = line.replace(keyWord,keyWords[keyWord])
        out.writelines(line)
        prev = currentIndetation
             
if len(global_indentation) != 0:
    out.writelines('\n'+function.makingIndenation(0))
    
out.close()