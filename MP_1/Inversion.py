import array as arr

def readFileIntoArray(fileName, inputType):
    retArr = arr.array(inputType)
    with open(fileName, 'rt') as f:
        for line in f:
            retArr.append(int(line))
    return retArr

def Inverse(inputArray, startIndex, endIndex):
    ret = 0
    #sanity check
    if (startIndex > endIndex) :
        #bad throw error plz
        raise InversionIndexError
    #base case
    if(endIndex - startIndex <= 1):
        if(inputArray[startIndex] > inputArray[endIndex]):
            #flip this
            temp = inputArray[startIndex]
            inputArray[startIndex] = inputArray[endIndex]
            inputArray[endIndex] = temp
            return 1
        else: #base case of 1
            return 0
    #left side

    subArrayLen = (endIndex - startIndex + 1)/2

    leftInverse = Inverse(inputArray, startIndex, endIndex - subArrayLen)
    #right side
    rightInverse = Inverse(inputArray, endIndex - subArrayLen + 1 , endIndex)

    #split inversion logic
    splitInverse = 0
    
    leftIndex = startIndex #leftStartingIndex
    rightIndex = endIndex - subArrayLen + 1 #rightStartingIndex
    leftSideRemain = rightIndex - leftIndex #subArrayLen
    rightSideRemain = endIndex - rightIndex + 1

    for i in range(0, endIndex - startIndex + 1):
        #print('i : ' + str(i) + '/' + str(endIndex - startIndex + 1))
        #print('leftIndex : ' + str(leftIndex))
        #print('leftsideRemain : ' + str(leftSideRemain))
        #print('rightIndex : ' + str(rightIndex))
        #print('rightSideRemain : ' + str(rightSideRemain))
        if ((inputArray[leftIndex] <= inputArray[rightIndex]) and leftSideRemain > 0): #case of not inverted
            if (leftIndex < len(invertedArray)-1):
                leftIndex += 1
            if (leftSideRemain > 0):
                leftSideRemain -= 1
        else: #case of inversion
            splitInverse += leftSideRemain
            #reorder the array in place
            #print ('rightIndex : ' + str(rightIndex))
            #print ('rightValue : ' + str(inputArray[rightIndex]))
            #print ('>before split flip : ' )
            #print (inputArray)
            rightValue = inputArray.pop(rightIndex)
            inputArray.insert(leftIndex, rightValue)
            #print ('>after split flip : ' )
            #print (inputArray)
            #print('rightSideRemain : ' + str(rightSideRemain))
            #print 
            leftIndex += 1
            if (rightIndex <= len(invertedArray)-1):
                rightIndex += 1
            if (rightSideRemain > 0):
                rightSideRemain -= 1
        if (leftSideRemain == 0 or rightSideRemain == 0):
            break
        
    ret = leftInverse + rightInverse + splitInverse
    return ret

#define exception
class Error(Exception):
   'Base class for other exceptions'
   pass

class InversionIndexError(Error):
   'Inversion function data input is invalid : endIndex is less than startIndex'
   pass

#MAIN PROGRAM
# fileName = 'IntegerArrayTest.txt'
# invertedArray = readFileIntoArray(fileName,'i')
# #print(invertedArray)
# print('result : ' + str(Inverse(invertedArray, 0, len(invertedArray) - 1)))
# print(invertedArray)

# fileName = 'IntegerArrayTest3.txt'
# invertedArray = readFileIntoArray(fileName,'i')
# #print(invertedArray)
# print('result : ' + str(Inverse(invertedArray, 0, len(invertedArray) - 1)))
# print(invertedArray)

# fileName = 'IntegerArrayTest4.txt'
# invertedArray = readFileIntoArray(fileName,'i')
# #print(invertedArray)
# print('result : ' + str(Inverse(invertedArray, 0, len(invertedArray) - 1)))
# print(invertedArray)

# fileName = 'IntegerArrayTest6.txt'
# invertedArray = readFileIntoArray(fileName,'i')
# #print(invertedArray)
# print('result : ' + str(Inverse(invertedArray, 0, len(invertedArray) - 1)))
# print(invertedArray)

# fileName = 'IntegerArray.txt'
# invertedArray = readFileIntoArray(fileName,'l')
# #print(invertedArray)
# print('result : ' + str(Inverse(invertedArray, 0, len(invertedArray) - 1)))