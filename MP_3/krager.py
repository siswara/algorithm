import array as arr
import re
import random
import copy

### use dictionary
def readGraphFileToDict(fileName):
    retDict = {}
    with open(fileName, 'rt') as f:
        for line in f:
            intSplit = re.split(r'[\s]\s*', line)
            retDict[intSplit[0]] = intSplit[1:len(intSplit)-1]
    return retDict

def minCut(graphIn, numberOfTrial):
    ret = 9999999999
    for i in range(0,numberOfTrial):
        tempGraph = copy.deepcopy(graphIn)
        tempMin = krager(tempGraph)
        print ('### temp min : ' + str(tempMin))
        if ret > tempMin:
            ret = tempMin
            #print (tempGraph)
    return ret

def krager(graphIn):
    ret = 0
    #print ('### graph nodes in the beginning algo completed : ')
    #print (graphIn)
    #min cut condition
    if len(graphIn) == 2 :
        ret = len(graphIn[graphIn.keys()[0]]) #the edges is indentical
        #print ('### ret : ' + str(ret))
        return ret
        #for i in graphIn.iterkeys():
    
    #naive implementation
    totalEdge = 0
    for i in graphIn.iterkeys():
        totalEdge += len(graphIn[i])

    indexOfMergedEdge = random.randint(0, totalEdge - 1)
    #print ('### totalEdge : ' + str(totalEdge))
    #print ('### indexOfMergedEdge : ' + str(indexOfMergedEdge))

    firstVertex = ''
    secondVertex = ''
    for i in graphIn.iterkeys():
        #print ('### vertex : ' + i)
        #print ('### number of edges : ' + str(len(graphIn[i])))
        if (indexOfMergedEdge <= len(graphIn[i])-1):
            firstVertex = i
            # print ('### graph['+1+'] : ')
            # print (graphIn)
            # print ('### graph['+i+']['+str(indexOfMergedEdge)+']=' + graphIn[i][indexOfMergedEdge])
            secondVertex = graphIn[i][indexOfMergedEdge]
            break
        else:
            indexOfMergedEdge -= len(graphIn[i])
            #print ('### indexOfMergedEdge : ' + str(indexOfMergedEdge))

    #print ('### firstVertex : ' + firstVertex)
    #print ('### secondVertex : ' + secondVertex)
    #merge and delete; and call back krager
    #new node
    newVertexName = firstVertex + '+' + secondVertex
    #print ('### newVertexName : ' + newVertexName)
    newEdges = copy.deepcopy(graphIn[firstVertex]) + copy.deepcopy(graphIn[secondVertex])
    
    #absorb self referencing
    for i in range(0, newEdges.count(firstVertex)):
        newEdges.remove(firstVertex)
    for i in range(0, newEdges.count(secondVertex)):
        newEdges.remove(secondVertex)

    #print ('### newEdges : ' )
    #print (newEdges)
    del graphIn[firstVertex]
    del graphIn[secondVertex]
    #update graph with new vertex naming
    for i in graphIn.iterkeys():
        for j in range(0, graphIn[i].count(firstVertex)):
            graphIn[i][graphIn[i].index(firstVertex)] = newVertexName
        for j in range(0, graphIn[i].count(secondVertex)):
            graphIn[i][graphIn[i].index(secondVertex)] = newVertexName
    #add new total vertex
    graphIn[newVertexName] = newEdges
    #recurse
    #print ('### graph nodes after algo completed : ')
    #print (graphIn.keys())
    ret = krager(graphIn)
    return ret

### -- retired
# def readFileIntoArray(fileName, inputType):
#     retVArr = arr.array(inputType)
#     retMArr = arr.array(inputType)
#     with open(fileName, 'rt') as f:
#         for line in f:
#             intSplit = re.split(r'[\s]\s*', line)
#             print (intSplit)
#             retVArr.append(int(intSplit[0]))
#             for i in range(1,len(intSplit)):
#                 if (intSplit[i] != ''):
#                     retMArr.append(int(intSplit[i]))
#     return retVArr, retMArr


fileName = 'kragerMinCut.txt'
graph = readGraphFileToDict(fileName)
#print (graph)
#print (minCut(graph, 0))
print ('### result of ['+str(len(graph))+'] iteration : ' + str(minCut(graph, len(graph))))