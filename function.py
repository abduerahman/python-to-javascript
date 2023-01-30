import re;

def convertingForloop(str):
    value = str.split(' ')
    value = convertRange(value[len(value) - 1])
    return 'for (let i =%d; i < %d; i += %d ) {' % (value[0],value[1],value[2])
    
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
    return len(str) - len(str.strip())

def makingIndenation(indentation):
    return ' '*(indentation)+'}'+'\n'

def varibleDeclration(declration,indentation):
    statment = declration.strip()
    s = re.search('(\W|\w)+ =',statment)
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