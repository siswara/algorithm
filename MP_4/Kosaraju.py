import array as arr
import re
import random
import copy
import sys
import resource
#--- GLOBAL ---#

#--- DEFINITION SECTION ---#
class Node:
    def __init__(self, index, finishTime, explored, nextNodes = [], previousNodes = []):
        self.index = index
        self.finishTime = finishTime
        self.explored = False
        self.nextNodes = nextNodes
        self.previousNodes = previousNodes
    def __str__(self):
        printStr = "index : " + str(self.index) + "\n"
        printStr += "finishTime : " + str(self.finishTime) + "\n"
        printStr += "explored : " + str(self.explored) + "\n"
        printStr += "nextNodes : "  
        for node in self.nextNodes:
            printStr += str(node.index) + ", "
        printStr = printStr[0: len(printStr) - 2]
        printStr += "\n"
        printStr += "previousNodes : "
        for node in self.previousNodes:
            printStr += str(node.index) + ", "
        printStr = printStr[0: len(printStr) - 2]
        printStr += "\n"
        return printStr.format(self)

def readGraphFileToNodesMap2(fileName):
    retDict = {}
    with open(fileName, 'rt') as f:
        for line in f:
            intSplit = re.split(r'[\s]\s*', line)
            fromIndex = int(intSplit[0])
            destinationIndex = int(intSplit[1])
            fromNode = None
            destNode = None
            try:
                fromNode = retDict[fromIndex]
            except:
                fromNode = Node(fromIndex, 0, False, set(), set())
                retDict[fromIndex] = fromNode
                
            try:
                destNode = retDict[destinationIndex]
            except:
                destNode = Node(destinationIndex, 0, False, set(), set())
                retDict[destinationIndex] = destNode

            fromNode.nextNodes.add(retDict[destinationIndex])
            destNode.previousNodes.add(retDict[fromIndex]) 
    return retDict

def readGraphFileToNodesMap(fileName):
    retDict = {}
    with open(fileName, 'rt') as f:
        for line in f:
            intSplit = re.split(r'[\s]\s*', line)
            fromIndex = int(intSplit[0])
            destinationIndex = int(intSplit[1])
            if (not (fromIndex in retDict.keys())):
                retDict[fromIndex] = Node(fromIndex, 0, False, [], [])
            if (not (destinationIndex in retDict.keys())):
                retDict[destinationIndex] = Node(destinationIndex, 0, False, [], [])
            retDict[fromIndex].nextNodes.append(retDict[destinationIndex])
            retDict[destinationIndex].previousNodes.append(retDict[fromIndex]) 
    return retDict

def KosarajuRecursive(graphIn):
    ret = []
    finishTimeCounter = [0]
    lastIndex = max(graphIn.keys())
    firstIndex = min(graphIn.keys())
    for i in range(lastIndex,firstIndex-1, -1):
        try:
            if (graphIn[i].explored == True):
                continue
            DFS(graphIn[i], finishTimeCounter)
        except:
            continue
    unExploreGraph(graphIn)
    reIndexedGraph = reIndexGraphWithFinishTime(graphIn)

    for i in range(lastIndex,firstIndex-1, -1):
        try:
            if (reIndexedGraph[i].explored == True):
                continue
            ret.append(DFScyclical(reIndexedGraph[i]))
        except:
            continue
    return ret

def DFScyclical(nodeIn):
    nodeIn.explored = True
    ret = 0
    for nextNode in nodeIn.nextNodes:
        if (nextNode.explored != True):
            ret += DFScyclical(nextNode)
    ret += 1
    return ret

def DFS(nodeIn, finishTimeCounter):
    # print (nodeIn)
    nodeIn.explored = True
    # explore next node
    for nextNode in nodeIn.previousNodes:
        if (nextNode.explored != True):
            DFS(nextNode, finishTimeCounter)
    finishTimeCounter[0] = finishTimeCounter[0]+1
    nodeIn.finishTime = finishTimeCounter[0]
    return 0

# #TODO : Iterative style
# def KosarajuIterative(graphIn):
#     ret = []
#     finishTimeCounter = [0]
#     lastIndex = max(graphIn.keys())
#     firstIndex = min(graphIn.keys())
#     for i in range(lastIndex,firstIndex-1, -1):
#         if (i in graphIn.keys()):
#             if (graphIn[i].explored == True):
#                 continue
#             DFSIterative(graphIn[i], finishTimeCounter)
#     unExploreGraph(graphIn)
#     reIndexGraphWithFinishTime(graphIn)
#     return ret

# #TODO : Iterative style
# def DFSIterative(nodeIn, finishTimeCounter):
#     currentNode = nodeIn
#     nodeChain = [] #keep track of steps made by iteration 
#     # while currentNode.explored == False:
#     #     currentNode.explored = True
#     #     nodeChain.append(currentNode)
#         #keep moving until no next or reach itself
#         #move backward
#     return

#--- HELPER FUNCTION ---#
def unExploreGraph(graphIn):
    for i in graphIn.keys():
        graphIn[i].explored = False
    return

def reIndexGraphWithFinishTime(graphIn):
    tempGraph = {}
    for i in graphIn.keys():
        tempGraph[graphIn[i].finishTime] = graphIn[i]
    return tempGraph

#--- MAIN LOOP ---#
sys.setrecursionlimit(2 ** 25)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

graphG = readGraphFileToNodesMap2("SCC.txt")
# for i in graphG.keys():
#    print(graphG[i])
SCC = KosarajuRecursive(graphG)
SCC.sort(reverse=True)
print (SCC[0:5])

#test data structure representation
#
#     /--> 2 -->
#   1      ^     4
#     \--> 3 -->
#

# graphG = {}
# graphG[4] = Node(4, 0, False, [], [])
# graphG[3] = Node(3, 0, False, [graphG[4]], [])
# graphG[2] = Node(2, 0, False, [graphG[4]], [])
# graphG[3].nextNodes.append(graphG[2])
# graphG[1] = Node(1, 0, False, [graphG[2], graphG[3]], [])
# graphG[4].previousNodes.append(graphG[2])
# graphG[4].previousNodes.append(graphG[3])
# graphG[2].previousNodes.append(graphG[1])
# graphG[2].previousNodes.append(graphG[3])
# graphG[3].previousNodes.append(graphG[1])

# print(graphG[1])
# print(graphG[2])
# print(graphG[3])
# print(graphG[4])