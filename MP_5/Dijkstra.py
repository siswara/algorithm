import array as arr
import re
import random
import copy
import sys
import resource

class Edge:
    def __init__(self, weight, endNode):
        self.weight = weight
        self.endNode = endNode #head and tail of nodes
    def __str__(self):
        printStr = "endNode : " + str(self.endNode) + ","
        printStr += "weight : " + str(self.weight)
        return printStr
        
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

def readGraphFileToNodesMap(fileName):
    retDict = {}
    with open(fileName, 'rt') as f:
        for line in f:
            intSplit = re.split(r'[\s]\s*', line)
            curIndex = int(intSplit[0])
            edges = []
            for i in range (1,len(intSplit)-1):
                vert = re.split(r',*', intSplit[i])
                #print (vert)
                tempVert = Edge(int(vert[1]), int(vert[0]))
                edges.append(tempVert)
            retDict[curIndex] = Node(curIndex, edges)
    return retDict

def SetDjikstraScore(graphIn, sourceNode):
    #init 
    for n in graphIn:
        graphIn[n].score = 1000000
    graphIn[sourceNode].score = 0
    
    dGraph = {}
    dGraph[sourceNode] = graphIn[sourceNode]
    dGraphSet = set()
    dGraphSet.add(sourceNode)

    while True:
        minScore = 1000000
        curMinNode = 0
        prevScore = 0
        #print ('#### dGraph')
        for node in dGraph:
            #print ('i : '+ str(node))
            for edge in dGraph[node].edges:
                weightFromStart = dGraph[node].score + edge.weight
                #print ('edge.endNode : ' + str(edge.endNode) + ', score : ' + str(weightFromStart) + ' ,isEndpoint absorb : ' + str(not edge.endNode in dGraphSet) + ' ,minscore : ' + str(minScore))

                if not edge.endNode in dGraphSet:
                    if weightFromStart < minScore:
                        minScore = weightFromStart#edge.weight
                        prevScore = dGraph[node].score
                        curMinNode = edge.endNode
                    #elif weightFromStart == minScore:
                        #print ('competing weight detected!')
        if minScore == 1000000:
            break
        else:
            #print added node to djikstra model
            #nodeScore = prevScore + minScore
            #print ('node added : ' + str(curMinNode) + ' ,score : ' + str(minScore))
            graphIn[curMinNode].score = minScore
            dGraph[curMinNode] = graphIn[curMinNode]
            dGraphSet.add(curMinNode)

    return

fileName = 'DijkstraData.txt'
graph = readGraphFileToNodesMap(fileName)
# for i in graph.keys():
#     print graph[i]
SetDjikstraScore(graph, 1)
# for i in graph.keys():
#     print (str(i) + ' - ' + str(graph[i].score))
print (graph[7].score)
print (graph[37].score)
print (graph[59].score)
print (graph[82].score)
print (graph[99].score)
print (graph[115].score)
print (graph[133].score)
print (graph[165].score)
print (graph[188].score)
print (graph[197].score)

#meh no
#7,37,59,82,99,115,133,165,188,197
# print (DijkstraShortes(graph,1,7))
# print (DijkstraShortes(graph,1,37))
# print (DijkstraShortes(graph,1,59))
# print (DijkstraShortes(graph,1,82))
# print (DijkstraShortes(graph,1,99))
# print (DijkstraShortes(graph,1,115))
# print (DijkstraShortes(graph,1,133))
# print (DijkstraShortes(graph,1,165))
# print (DijkstraShortes(graph,1,188))
# print (DijkstraShortes(graph,1,197))

