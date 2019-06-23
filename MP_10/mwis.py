import argparse

parser = argparse.ArgumentParser('This code is to compute the max weight independent set of path graph')
parser.add_argument(dest='filename', metavar='filename')
args = parser.parse_args()
print(args.filename)

def readFile(fileName):
    ret = []
    ret.append(0) #to make element index = lineNum
    with open(fileName, 'rt') as f:
        lineNum = 0
        for line in f:
            line = line.replace('\n','')
            if lineNum == 0:
                print(line)
            else:
                ret.append((int(line), str(lineNum)))
            lineNum += 1
    return ret

if args.filename == '':
    print ('provide filename')
else:
    #mwis
    path = readFile(args.filename)
    wis = [] #weight indendent set
    wis.append(0)
    wis.append(path[1][0])
    i = 2
    for i in range(2,len(path)):
        #print (i)
        wis.append(max(wis[i-1], wis[i-2] + path[i][0]))
    print (wis)

    #rebuild algo
    selectedVertex = []
    i = len(path)-1
    #for i in range(len(path)-1, 0, -1):
    while i >= 1:
        #print (i)
        if (wis[i-1] >= wis[i-2] + path[i][0]):
            i = i-1
        else:
            selectedVertex.append(path[i][1])
            i = i-2
        
    print(selectedVertex)
    #1, 2, 3, 4, 17, 117, 517, and 997
    outSelectedVertex = []
    outSelectedVertex.append(1 if '1' in selectedVertex else 0)
    outSelectedVertex.append(1 if '2' in selectedVertex else 0)
    outSelectedVertex.append(1 if '3' in selectedVertex else 0)
    outSelectedVertex.append(1 if '4' in selectedVertex else 0)
    outSelectedVertex.append(1 if '17' in selectedVertex else 0)
    outSelectedVertex.append(1 if '117' in selectedVertex else 0)
    outSelectedVertex.append(1 if '517' in selectedVertex else 0)
    outSelectedVertex.append(1 if '997' in selectedVertex else 0)
    print (''.join(str(x) for x in outSelectedVertex))


