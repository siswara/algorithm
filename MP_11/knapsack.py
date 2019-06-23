import argparse

parser = argparse.ArgumentParser('This code is to compute the max value for knapsack problem')
parser.add_argument(dest='filename', metavar='filename')
args = parser.parse_args()
print(args.filename)

def readFile(fileName):
    sackSize = 0
    ret = []
    ret.append((0,0)) #move to 1
    with open(fileName, 'rt') as f:
        lineNum = 0
        for line in f:
            line = line.replace('\n','')
            lineSplit = line.split()
            if lineNum == 0:    
                sackSize = int(lineSplit[0])
            else:
                #value, weight
                ret.append((int(lineSplit[0]), int(lineSplit[1])))
            lineNum += 1
    return sackSize, ret

def bgKnapsack2(sackSize, sackItems):
    ret = 0
    sack = []
    #init
    sack.append([])
    for x in range(0,sackSize+1):
        sack[0].append(0)

    #main knapsack
    for i in range(1, len(sackItems)):
        firstRun = False
        for x in range(0, sackSize+1):
            if not firstRun:
                sack.append([])
                firstRun = True
            case1 = sack[len(sack)-1-1][x] #not including current item
            case2 = 0
            if (x-sackItems[i][1]) > 0 :
                case2 = sack[len(sack)-1-1][x-sackItems[i][1]] + sackItems[i][0]
            sack[len(sack)-1].append(max(case1, case2))
        if len(sack) == 3:
            sack.pop(0)
    #print (sack)
    ret = sack[1][sackSize]
    return ret

def bgKnapsack(sackSize, sackItems):
    ret = 0
    sack = []
    #idea
    #[i] --> list of ([weights] , value) 

    #init
    sack.append([(range(0,sackSize+1), 0)])

    #main knapsack
    for i in range(1, len(sackItems)):
        print ('### observing item # : ' + str(i))
        firstRun = False
        for x in range(0, sackSize+1):
            if not firstRun:
                sack.append([([], 0)])
                firstRun = True
            case1 = 0
            case2 = 0
            #look for x in sack [i-1]
            #print (len(sack)-1-1)
            for sacSum in sack[len(sack)-1-1]:
                if x in sacSum[0]:
                    case1 = sacSum[1]
                    break
            if (x-sackItems[i][1]) > 0 :
                for sacSum in sack[len(sack)-1-1]:
                    if x-sackItems[i][1] in sacSum[0]:
                        case2 = sacSum[1] + sackItems[i][0]
                        break
            currSum = max(case1, case2)
            sumFound = False
            for sacSum in sack[len(sack)-1]:
                if sacSum[1] == currSum:
                    sacSum[0].append(x)
                    sumFound = True
                    break
            if not sumFound:
                sack[len(sack)-1].append(([x], currSum))
        #to minimize the array, delete th first array when there is 3 array
        if len(sack) == 3:
            sack.pop(0)
    #print (sack)
    #look for ret
    for sacSum in sack[1]:
        if sackSize in sacSum[0]:
            ret = sacSum[1]
    return ret

def smKnapsack(sackSize, sackItems):
    ret = 0
    sack = []
    #init
    sack.append([])
    for x in range(0,sackSize+1):
        sack[0].append(0)

    #main knapsack
    for i in range(1, len(sackItems)):
        for x in range(0, sackSize+1):
            if i >= len(sack):
                sack.append([])
            case1 = sack[i-1][x] #not including current item
            case2 = 0
            if (x-sackItems[i][1]) > 0 :
                case2 = sack[i-1][x-sackItems[i][1]] + sackItems[i][0]
            sack[i].append(max(case1, case2))
    #print (sack)
    ret = sack[len(sackItems)-1][sackSize]
    return ret

sackSize, sackItems = readFile(args.filename)
print (sackSize)
optimumValue2 = bgKnapsack2(sackSize, sackItems)
print (optimumValue2)
optimumValue = smKnapsack(sackSize, sackItems)
print (optimumValue)