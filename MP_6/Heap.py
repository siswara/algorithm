import array as arr
import re
import random
import copy
import sys
import resource


def readFilesAndComputeMedian(fileName):
    ret = 0
    higherHalf = MinHeap([])
    lowerHalf = MaxHeap([])
    with open(fileName, 'rt') as f:
        for line in f:
            curVal = int(line)
            #print ('incoming val : ' + str(curVal))
            if (lowerHalf.peekMax() == None or higherHalf.peekMin() == None): #1st & 2nd initialize lookup
                if lowerHalf.peekMax() == None:
                    lowerHalf.add(curVal)
                    ret += lowerHalf.peekMax()
                else:
                    lowerHalf.add(curVal)
                    higherHalf.add(lowerHalf.getMax())
                    ret += lowerHalf.peekMax()
                #print ('MID : ' + str(lowerHalf.peekMax()))
            else:
                highVal = higherHalf.peekMin()
                lowVal = lowerHalf.peekMax()
                if (highVal > curVal):
                    lowerHalf.add(curVal)
                    if len(lowerHalf.heap) - 1 > len(higherHalf.heap):
                        higherHalf.add(lowerHalf.getMax())    
                else:
                    higherHalf.add(curVal)
                    if len(higherHalf.heap) > len(lowerHalf.heap):
                        lowerHalf.add(higherHalf.getMin())
                #print ('lowerHeap : ')
                #print (lowerHalf.heap)
                #print ('higherHeap : ')
                #print (higherHalf.heap)
                #print ('MID : ' + str(lowerHalf.peekMax()))
                ret += lowerHalf.peekMax()
        ret = ret%10000
    return ret

class MaxHeap:
    def __init__(self, heap):
        self.heap = heap
    def add(self,inputElement):
        curIndex = len(self.heap)
        self.heap.append(inputElement)
        #bubble up
        #who is my parent
        while True:
            parentIndex = int((curIndex - 1)/2)
            if (parentIndex < 0):
                break
            elif (self.heap[parentIndex] < self.heap[curIndex]):
                #flip
                temp = self.heap[parentIndex]
                self.heap[parentIndex] = self.heap[curIndex]
                self.heap[curIndex] = temp
                curIndex = parentIndex
            else :
                break
        return
    def getMax(self):
        if (len(self.heap) == 0):
            return None

        ret = self.heap[0]
        lastIndex = len(self.heap) - 1
        self.heap[0] = self.heap[lastIndex]
        del self.heap[lastIndex]
        curIndex = 0
        while True:
            leftChildIndex = (curIndex * 2) + 1
            rightChildIndex = (curIndex * 2) + 2
            childIndex = 0
            if (leftChildIndex > (len(self.heap) - 1)):
                break
            elif (leftChildIndex == (len(self.heap) - 1)):
                if (self.heap[curIndex] >= self.heap[leftChildIndex]):
                    break
                else:
                    childIndex = leftChildIndex
            else:   
                if (self.heap[curIndex] >= self.heap[leftChildIndex] and self.heap[curIndex] >= self.heap[rightChildIndex]):
                    break
                else:
                    if (self.heap[leftChildIndex] > self.heap[rightChildIndex]):
                        #flip
                        childIndex = leftChildIndex
                    else:
                        childIndex = rightChildIndex
            temp = self.heap[childIndex]
            self.heap[childIndex] = self.heap[curIndex]
            self.heap[curIndex] = temp
            curIndex = childIndex
        return ret
    def peekMax(self):
        if (len(self.heap) == 0):
            return None
        ret = self.heap[0]
        return ret

class MinHeap:
    def __init__(self, heap):
        self.heap = heap
    def add(self,inputElement):
        curIndex = len(self.heap)
        self.heap.append(inputElement)
        #bubble up
        #who is my parent
        while True:
            parentIndex = int((curIndex - 1)/2)
            if (parentIndex < 0):
                break
            elif (self.heap[parentIndex] > self.heap[curIndex]):
                #flip
                temp = self.heap[parentIndex]
                self.heap[parentIndex] = self.heap[curIndex]
                self.heap[curIndex] = temp
                curIndex = parentIndex
            else :
                break
        return
    def getMin(self):
        if (len(self.heap) == 0):
            return None

        ret = self.heap[0]
        lastIndex = len(self.heap) - 1
        self.heap[0] = self.heap[lastIndex]
        del self.heap[lastIndex]
        curIndex = 0
        while True:
            leftChildIndex = (curIndex * 2) + 1
            rightChildIndex = (curIndex * 2) + 2
            childIndex = 0
            if (leftChildIndex > (len(self.heap) - 1)):
                break
            elif (leftChildIndex == (len(self.heap) - 1)):
                if (self.heap[curIndex] <= self.heap[leftChildIndex]):
                    break
                else:
                    childIndex = leftChildIndex
            else:   
                if (self.heap[curIndex] <= self.heap[leftChildIndex] and self.heap[curIndex] <= self.heap[rightChildIndex]):
                    break
                else:
                    if (self.heap[leftChildIndex] < self.heap[rightChildIndex]):
                        #flip
                        childIndex = leftChildIndex
                    else:
                        childIndex = rightChildIndex
            temp = self.heap[childIndex]
            self.heap[childIndex] = self.heap[curIndex]
            self.heap[curIndex] = temp
            curIndex = childIndex
        return ret
    def peekMin(self):
        if (len(self.heap) == 0):
            return None
        ret = self.heap[0]
        return ret

fileName = 'Median.txt'
print (readFilesAndComputeMedian(fileName))

