#must use python3
import argparse
import heapq
from treelib import Node, Tree

parser = argparse.ArgumentParser('This code is to compute the minimum huffman encoding')
parser.add_argument(dest='filename', metavar='filename')
args = parser.parse_args()
print(args.filename)

def readFile(fileName):
    ret = []
    with open(fileName, 'rt') as f:
        lineNum = 0
        for line in f:
            line = line.replace('\n','')
            if lineNum == 0:
                print(line)
            else:
                heapq.heappush(ret, (int(line), str(lineNum)))
            lineNum += 1
    return ret

def huffman(codes):
    ret = None
    mergeOrder = []

    #huffman code 
    while True:
        if len(codes) == 1:
            break
        firstCode = heapq.heappop(codes)
        secondCode = heapq.heappop(codes)

        mCode = '(' + firstCode[1] + '+' + secondCode[1] + ')'
        mOccurance = firstCode[0] + secondCode[0]
        heapq.heappush(codes, (mOccurance, mCode))
        mergeOrder.append((firstCode[1],secondCode[1],mCode))
    
    #rebuild
    treeMap = {}
    for mergeAct in mergeOrder:
        tempTree = Tree()
        tempTree.create_node(mergeAct[2], mergeAct[2]) #root
        if mergeAct[0] in treeMap:
            tempTree.paste(mergeAct[2], treeMap[mergeAct[0]])
        else:
            tempTree.create_node(mergeAct[0], mergeAct[0], parent=mergeAct[2])
        if mergeAct[1] in treeMap:
            tempTree.paste(mergeAct[2], treeMap[mergeAct[1]])
        else:
            tempTree.create_node(mergeAct[1], mergeAct[1], parent=mergeAct[2])
        treeMap[mergeAct[2]] = tempTree
    
    ret = treeMap[mergeOrder[len(mergeOrder)-1][2]]
    return ret

if args.filename == '':
    print ('provide filename')
else:
    codes = readFile(args.filename)
    
    finalTree = huffman(codes)
    #treeMap Print
    #finalTree.show()
    #max code len
    print ('max : ' + str(finalTree.depth()))
    #min code len
    #get min(all leaves level)
    treeRoot = finalTree.root
    treeLeaves = finalTree.leaves(treeRoot)
    leavesLevel = []
    for leaf in treeLeaves:
        leavesLevel.append(finalTree.depth(leaf))
    print ('min : ' + str(min(leavesLevel)))