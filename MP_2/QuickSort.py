import array as arr

def readFileIntoArray(fileName, inputType):
    retArr = arr.array(inputType)
    with open(fileName, 'rt') as f:
        for line in f:
            retArr.append(int(line))
    return retArr

def flipElement(inputArray, index1, index2):
    temp = inputArray[index1]
    inputArray[index1] = inputArray[index2]
    inputArray[index2] = temp
    return

#add extra condition
#pivot :
#   - first
#   - last
#   - mid
def partition(inputArray, startIndex, endIndex, pivot='first'):
    # print ('### startIndex :' + str(startIndex))
    # print ('### endIndex : ' + str(endIndex))
    # print ('### anaylzed array')
    # print (inputArray[startIndex:endIndex + 1])
    ret = 0
    #base case
    if (endIndex - startIndex < 1):
        return 0
    
    if (startIndex < endIndex):
        ret = (endIndex - startIndex + 1) - 1 #m-1
        # print ('### num of m -1 : ' + str(ret))
    
    #determine pivot
    pivotIndex = 0
    if (pivot == 'first'):
        pivotIndex = startIndex
    elif (pivot == 'last'):
        pivotIndex = endIndex
    elif (pivot == 'mid'):
        #additional logic
        midIndex = startIndex + (endIndex - startIndex) / 2
        firstVal = inputArray[startIndex]
        secondVal = inputArray[midIndex]
        thirdVal = inputArray[endIndex]
        if (firstVal < secondVal < thirdVal) or (thirdVal < secondVal < firstVal):
            pivotIndex = midIndex
        elif (secondVal < firstVal < thirdVal) or (thirdVal < firstVal < secondVal) :
            pivotIndex = startIndex
        elif (firstVal < thirdVal < secondVal) or (secondVal < thirdVal < firstVal) : 
            pivotIndex = endIndex
        else :
            pivotIndex = startIndex
            #pivotIndex = startIndex + (endIndex - startIndex) / 2
    else : #default is first
        pivotIndex = startIndex

    #main function
    #move pivot to beginning of the array
    # print ('### pivotIndex : ' + str(pivotIndex))
    # print ('### pivotValue : ' + str(inputArray[pivotIndex]))
    flipElement(inputArray, pivotIndex, startIndex)

    #init
    lessIndex = startIndex + 1
    greaterIndex = startIndex + 1
    
    # print ('### before partition')
    # print (inputArray)

    for greaterIndex in range(startIndex + 1, endIndex + 1):
        #print ('### greaterIndex : ' + str(greaterIndex))
        if inputArray[greaterIndex] < inputArray[startIndex]:
            flipElement(inputArray, greaterIndex, lessIndex)
            lessIndex += 1
    
    flipElement(inputArray, startIndex, lessIndex - 1)
    # print ('### after partition')
    # print (inputArray[startIndex:endIndex+1])
    # print ('### startIndex : ' + str(startIndex))
    # print ('### lessIndex : ' + str(lessIndex))
    #print ('### greaterIndex : ' + str(greaterIndex))
    #recursive left
    ret += partition(inputArray, startIndex, lessIndex - 2, pivot)
    #recursive right
    ret += partition(inputArray, lessIndex, endIndex, pivot)
    #print(inputArray)
    return ret

fileName = 'QuickSort.txt'
inputArray = readFileIntoArray(fileName, 'i')
#print (inputArray)
print ('### first')
print (partition(inputArray, 0, len(inputArray) - 1, 'first'))
#print (inputArray)

inputArray = readFileIntoArray(fileName, 'i')
# #print (inputArray)
print ('### last')
print (partition(inputArray, 0, len(inputArray) - 1, 'last'))
#print (inputArray)

inputArray = readFileIntoArray(fileName, 'i')
#print (inputArray)
print ('### mid')
print (partition(inputArray, 0, len(inputArray) - 1, 'mid'))
#print (inputArray)