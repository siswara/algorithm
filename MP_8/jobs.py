import array as arr
import copy
import sys
import resource
import argparse
from operator import attrgetter

parser = argparse.ArgumentParser(description="Compute completion time for list of jobs in [weight] [length] format")
parser.add_argument(dest="filename", metavar="filename")

class Job:
    def __init__(self, weight, length, score):
        self.weight = int(weight)
        self.length = int(length)
        self.score = int(score)
    def __str__(self):
        return 'weight:{0.weight!s}, legth:{0.length!s}, score:{0.score!s}'.format(self)

def readFiles(fileName):
    ret = []
    with open(fileName, 'rt') as f:
        lineCount = 0
        for line in f:
            if lineCount == 0:
                print ("job count " + line)
            else:
                textSplit = line.split()
                tempJob = Job(textSplit[0], textSplit[1], 0)
                ret.append(tempJob)
            lineCount = lineCount + 1
    return ret

def setDifferenceScore(arrayOfJobs):
    for job in arrayOfJobs:
        job.score = job.weight - job.length
    return

def setRatioScore(arrayOfJobs):
    for job in arrayOfJobs:
        job.score = float(job.weight) / float(job.length)
    return

def printJob(arrayOfJobs):
    for job in arrayOfJobs:
        print (job)
    return

def calculateCompletionTime(arrayOfJobs):
    ret = 0
    sumOfLenght = 0
    for job in arrayOfJobs:
        sumOfLenght += job.length
        ret += sumOfLenght * job.weight
    return ret

args = parser.parse_args()
print (args.filename)

if args.filename != "" :
    arrayOfJobs = readFiles(args.filename)#'input_random_10_40.txt')#'jobs.txt')
    setDifferenceScore(arrayOfJobs)
    sortedJobsTie = sorted(arrayOfJobs, key=lambda j:j.weight, reverse=True)
    sortedJobs = sorted(sortedJobsTie, key=lambda j:j.score, reverse=True)
    print ("completion time using different : " + str(calculateCompletionTime(sortedJobs)))

    setRatioScore(arrayOfJobs)
    sortedJobsTie = sorted(arrayOfJobs, key=lambda j:j.weight, reverse=True)
    sortedJobs = sorted(sortedJobsTie, key=lambda j:j.score, reverse=True)
    #printJob(sortedJobs)
    print ("completion time using ratio : " + str(calculateCompletionTime(sortedJobs)))
else :
    print ("please supply filename")

