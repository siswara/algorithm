import array as arr
import copy
import sys
import resource

def readFilesAndReturnSorted(fileName):
    ret = []
    with open(fileName, 'rt') as f:
        for line in f:
            ret.append(int(line))
    # print ret
    ret.sort()
    return ret

def calc2Sum(tMin, tMax, sortedList):
    ret = 0 #all possible combination
    # tMin < x+y <tMax
    combinations = set()
    for x in sortedList:
        #look for y
        yMin = tMin-x
        yMax = tMax-x
        #binary search yMin - find closest
        minIndex = binarySearch(yMin, sortedList, False)
        maxIndex = binarySearch(yMax, sortedList, True)
        # print ('### x : ' + str(x))
        # print ('### minIndex ' + str(minIndex) + ', maxIndex : ' + str(maxIndex))
        # print ('### valueMinIndex ' + str(sortedList[minIndex]) + ', valueMaxIndex : ' + str(sortedList[maxIndex]))
        for yIndex in range(minIndex, maxIndex + 1):
            # xy = str(x) + ',' + str(sortedList[yIndex]) 
            # yx = str(x) + ',' + str(sortedList[yIndex]) 
            # try:
            #     combinations.add(xy)
            # finally:
            #     pass
            # try:
            #     combinations.add(yx)
            # finally:
            #     pass
            t = x + sortedList[yIndex]
            # print (t)
            try:
                if tMin <= t <= tMax:
                    combinations.add(t)
            finally:
                pass
        #binary search yMax - find closest 
        ret = len(combinations)
    return ret

def binarySearch(searchElement, sortedList, ceil):
    ret = 0
    curIndex = len(sortedList) / 2
    startIndex = 0
    endIndex = len(sortedList)
    count = 0
    while True:
    # while count < 6:
        # print ('### curIndex : ' + str(curIndex))
        # print ('### startIndex : ' + str(startIndex))
        # print ('### endIndex : ' + str(endIndex))
        # print ('------')
        if searchElement == sortedList[curIndex]:
            # print ('### match : ' + str(curIndex))
            ret = curIndex
            break
        elif searchElement > sortedList[curIndex]:
            startIndex = curIndex
            curIndex = curIndex + ((endIndex - startIndex)/2)
            if (curIndex == endIndex or curIndex == startIndex):
                ret = curIndex
                break
        elif searchElement < sortedList[curIndex]:
            endIndex = curIndex
            curIndex = startIndex + ((endIndex - startIndex)/2)
            if (curIndex == startIndex or curIndex == endIndex):
                ret = curIndex
                break
        count += 1
        #pass
        if ceil:
            ret += 1
    return ret

fileName = '2sum.txt'
sortedList = readFilesAndReturnSorted(fileName)
# print (sortedList)
print (calc2Sum(-10000,10000,sortedList))

testSorted = [-5,-2,0,2,5,7,10]
print (testSorted)
# # print (binarySearch(-5, testSorted))
# # print (binarySearch(-2, testSorted))
# # print (binarySearch(0, testSorted))

# # print (binarySearch(2, testSorted))
# # print (binarySearch(5, testSorted))
# # print (binarySearch(7, testSorted))
# # print (binarySearch(10, testSorted))

# # print (binarySearch(1, testSorted))
# # print (binarySearch(3, testSorted))
# # print (binarySearch(4, testSorted))
# # print (binarySearch(6, testSorted))
# print (binarySearch(-3, testSorted))