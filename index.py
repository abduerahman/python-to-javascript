from keyWords import keyWords,BreakKeyWords
from function import convertingForloop,removingIndentation
import function,datetime,pathlib,sys,re

dirPath = pathlib.Path().resolve()

inputFile = sys.argv[1]
outFileName = sys.argv[2]


file = open(inputFile,'r')
out = open(outFileName+'.js','w')

global_indentation = []
global_varible = []

prev = 0

lineNumber = 0
for line in file.readlines():
    if len(line.strip()) > 0 and lineNumber >= 5:
        currentIndetation = removingIndentation(line)
        
        if currentIndetation < prev :
            praketIndentation = 100000
            while praketIndentation > currentIndetation-1:
                praketIndentation = global_indentation.pop()
                if(praketIndentation == currentIndetation - 1):
                   global_indentation.append(praketIndentation)
                   break
                out.writelines(function.makingIndenation(praketIndentation))
                if(len(global_indentation) == 0):
                    break
   

        for i in BreakKeyWords:
            if(line.count(i) > 0):
                global_indentation.append(currentIndetation)
        
        if (line.count('for ')) > 0 and line.count('range(') > 0:
            line = ' '* (currentIndetation -1) + convertingForloop(line,currentIndetation)+'\n'
            
        elif(line.count('for ') ==0 and line.count('if ') == 0 and  function.varibleDeclration(line,currentIndetation) != None):
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
        if (re.search('(else if|if)\W+',line) != None):
            line = function.convertingIfStatment(line,currentIndetation)

        out.writelines(line)
        prev = currentIndetation
    lineNumber += 1

for i in range(len(global_indentation)):
    praket = global_indentation.pop()
    out.writelines(function.makingIndenation(praket))