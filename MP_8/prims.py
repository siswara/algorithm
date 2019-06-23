import argparse
import copy

parser = argparse.ArgumentParser(description="Compute overall cost of minimum spanning tree of graph")
parser.add_argument(dest="filename", metavar="filename")
args = parser.parse_args()
print (args.filename)

class Edge:
    def __init__(self, startNode, endNode, weight):
        self.weight = int(weight)
        self.startNode = startNode
        self.endNode = endNode #head and tail of nodes
    def __str__(self):
        return "{0.startNode!s} - {0.endNode!s} with weight {0.weight!s}".format(self)
        
class Node:
    def __init__(self, node, edges):
        self.node = node
        self.edges = edges
        self.score = 10000000
    def __str__(self):
        printStr = "node : " + str(self.node) + "\n"
        printStr += "vertexs : \n"
        for edge in self.edges:
            printStr += "[" + str(edge.endNode) + ',' + str(edge.weight) + "]" 
        return printStr

def readFiles(fileName):
    retEdges = []
    retNodes = set()
    with open(fileName, 'rt') as f:
        lineCount = 0
        for line in f:
            textSplit = line.split()
            if lineCount == 0:
                print ("# of nodes " + textSplit[0])
                print ("# of edges " + textSplit[1])
            else:
                tempEdge = Edge(textSplit[0],textSplit[1],textSplit[2])
                retEdges.append(tempEdge)
                retNodes.add(textSplit[0])
                retNodes.add(textSplit[1])
            lineCount = lineCount + 1
    return retEdges, retNodes

#do sorted heap on 
def isNodeInChain(nodeChains, firstNode, secondNode):
    retIsInSameChain = False
    retFirstChain = None #contains the firstNode
    retSecondChain = None #contains the secondNode
    for chain in nodeChains:
        if (firstNode in chain):
            retFirstChain = chain
        if (secondNode in chain):
            retSecondChain = chain
    if (retFirstChain != None and retSecondChain != None 
        and  retFirstChain == retSecondChain):
        retIsInSameChain = True
    return retIsInSameChain, retFirstChain, retSecondChain

def combineChain(nodeChains, firstChain, secondChain):
    combineChain = firstChain.union(secondChain)
    print (combineChain)
    nodeChains.append(combineChain)
    nodeChains.remove(firstChain)
    nodeChains.remove(secondChain)
    return

if (args.filename != ''):
    edges, nodeSet = readFiles(args.filename)
    print (len(nodeSet))
    print (len(edges))
    
    #sorted edges
    sortedEdge = sorted(edges, key=lambda edge:edge.weight, reverse=True)
    print (len(sortedEdge))
    absorbedNode = [] #set()
    totalMstLength = 0
    mst = []

    while True:
        #print (len(sortedEdge))
        if len(sortedEdge) == 0:
            break
        observeEdge = sortedEdge.pop()
        isInSameChain, firstChain, secondChain = isNodeInChain(absorbedNode, observeEdge.startNode, observeEdge.endNode)
        #print (isInSameChain)
        #print (firstChain)
        #print (secondChain)
        if observeEdge.startNode == observeEdge.endNode:
            continue
        elif isInSameChain:
            continue
        else: #valid
            if firstChain == None and secondChain == None:
                tempChain = set([observeEdge.startNode, observeEdge.endNode])
                absorbedNode.append(tempChain)
            elif firstChain != None and secondChain == None:
                #add to firstChain
                firstChain.add(observeEdge.startNode)
                firstChain.add(observeEdge.endNode)
            elif firstChain == None and secondChain != None:
                secondChain.add(observeEdge.startNode)
                secondChain.add(observeEdge.endNode)
            elif firstChain != None and secondChain != None:
                combineChain(absorbedNode, firstChain, secondChain)
            totalMstLength += observeEdge.weight
            mst.append(observeEdge)   
    print ("### totalMstLength : " + str(totalMstLength))
else:
    print ('please specify graph file!')
