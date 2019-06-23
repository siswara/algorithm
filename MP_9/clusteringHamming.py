import argparse

parser = argparse.ArgumentParser(description="Compute clustering of graph based on closest distance. Calculate the number of clustring to get k distance to hemming way disance 3")
parser.add_argument(dest="filename", metavar="filename")
args = parser.parse_args()
print (args.filename)

class Point:
    def __init__(self, label, group):
        self.label = label
        self.group = group

def readFile(fileName):
    ret = {}
    retOrderedClosest = []
    #retSet = set()
    retPoints = {}
    retGroups = {}
    bitmask = []
    numOfBits = 0
    debugBitMaskRet = {}
    with open(fileName, 'rt') as f:
        lineNum = 0
        for line in f:
            if lineNum == 0:
                print ("# of nodes " + line.replace("\n",""))
                lineSplit = line.split(" ")
                numOfBits = int(lineSplit[1])
                i = 0
                for i in range(numOfBits):
                    firstMask = 1 << i
                    bitmask.append(firstMask)
                    for j in range( i + 1, numOfBits):
                        secondMask = 1 << j
                        bitmask.append(firstMask ^ secondMask)
            else:
                if lineNum % 50000 == 0:
                    print (lineNum)
                cBin = line.replace(" ","").replace("\n","")
                lineBin = '0b'+line.replace(" ","").replace("\n","")
                iBin = int(lineBin, 2)
                
                retPoints[lineNum] = Point(lineNum, lineNum)
                retGroups[lineNum] = set([lineNum])

                #bitmask logic
                for bm in bitmask:
                    masked = bm | iBin
                    maskedAddMask = int('0b'+format(masked, '0' + str(numOfBits) + 'b')+format(bm, '0' + str(numOfBits) + 'b'),2)
                    try:
                        debugBitMaskRet[maskedAddMask].append(lineNum)
                    except:
                        debugBitMaskRet[maskedAddMask] = [lineNum]
            lineNum += 1
        ret = debugBitMaskRet
        for key in ret.keys():
            retOrderedClosest.append(ret[key])
        retOrderedClosest = sorted(retOrderedClosest, key=lambda group:len(group), reverse=True)
    return ret, retOrderedClosest, retPoints, retGroups

def getGroup(points, label):
    return points[label].group

def mergeGroup(points, groups, group1Head, group2Head):
    group1 = groups[group1Head]
    group2 = groups[group2Head]
    if (len(group1) >= len(group2)):
        #use group1
        for label in group2:
            group1.add(label)
            points[label].group = group1Head
        del groups[group2Head]        
    else:
        #use group2
        for label in group1:
            group2.add(label)
            points[label].group = group2Head
        del groups[group1Head]
    return

distanceMap, minDistGroup, points, groups = readFile(args.filename)

for labels in minDistGroup:
    #for every grouping bigger than 1, merge into groups
    if len(labels) > 1:
       #1 node is the main group we want to use
       destGroupHead = points[labels[0]].group
       for c in range(1, len(labels)):
           curGroupHead = getGroup(points, labels[c])
           if curGroupHead != destGroupHead:
               #print (str(curGroupHead) + ' , ' + str(destGroupHead))
               mergeGroup(points, groups, destGroupHead, curGroupHead)
               destGroupHead = points[labels[0]].group

print (groups)
print ('# of groupings : ' + str(len(groups.keys())))