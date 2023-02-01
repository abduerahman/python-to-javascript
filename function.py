import re;

globalIndenation = 4

def convertingForloop(str,indentation):
    value = str.split(' ')
    value = convertRange(value[len(value) - 1])
    return ' '*(indentation*globalIndenation)+'for (let i =%d; i < %d; i += %d ) {' % (value[0],value[1],value[2])
    
def convertRange(str):
    r = re.search('\(',str).span()
    r2 = re.search('\)',str).span()
    return initilizeValues(str[r[1]:r2[0]])

def initilizeValues(str):
    values = str.split(',')
    value = []
    if(len(values) == 3):
        return [int(i) for i in values]
    else:

        if len(values) == 1:
            value.append(0)
            value.append(int(values[0]))
            value.append(1)
        else:
            value.append(int(values[0]))
            value.append(int(values[1]))
            value.append(1)
    return value


def removingIndentation(str):
    return int( (len(str) - len(str.strip())) / globalIndenation)

def makingIndenation(indentation):
    return ' '*(indentation*globalIndenation)+'}'+'\n'

def varibleDeclration(declration,indentation):
    statment = declration.strip()
    s = re.search('\w+ *= *(\w+|\W+)',statment)
    if s != None:
        return [' '*(indentation-1)+'let '+statment,statment[0:statment.index('=')].replace(' ',''),indentation]
    return None

def gettingParmater(statment,global_varible,indenation):
    r = re.search('\(',statment).span()
    r2 = re.search('\)',statment).span()   
    statment = statment[r[1]:r2[0]].split(',')
    for s in statment:
        global_varible.append([s,indenation+4])
    return global_varible

def convertingIfStatment(string,indentation):
    start = re.search('(else if|if)\W+',string).span()
    if(start != None):
       return  (' '*int(indentation))+string[0:start[1]]+ '('+ string[start[1]:len(string) - 2] + ' ) {' +'\n'
