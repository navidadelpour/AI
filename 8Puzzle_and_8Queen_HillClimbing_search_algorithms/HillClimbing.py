from NPuzzleProblem import NPuzzleProblem
from NQueenProblem import NQueenProblem
import random
import math
from pprint import pprint
import time
import sys

def hillClimbing(problem, hardrate):
    t0 = time.time()
    problem.generateRandomBoard(hardrate)
    initialH = problem.heuristic()
    current = (problem, initialH,[])
    
    while(True):
        successors = current[0].getSuccessors()
        successor = successors[0]
        if successor[1] >= current[1]:
            answer = current
            break
        current = (successor[0], successor[1], current[2] + successor[2])

    time_elapsed = time.time() - t0
    accuracy = 1 - float(answer[1]) / float(initialH) if initialH and answer[1] else 1
    isGoal = answer[0].isGoal()

    answer = answer + (isGoal, accuracy, problem, time_elapsed)
    return answer

def solve(testNum, problem, trace):
    trueSum = 0
    overallAccuracy = 0
    overallTime = 0
    hardrate = 20
    for i in range (testNum):
        solution, h, path, isGoal, accuracy, initialState, time_elapsed = hillClimbing(problem, hardrate)
        if(isGoal):
            trueSum += 1
        overallAccuracy += accuracy
        overallTime += time_elapsed
        if(trace):
            print("------------------------------------------------")
            print(initialState.getState(), initialState.heuristic())
            print(solution.getState(), solution.heuristic())
            print(path)
            print(isGoal)
            print('%.2f' % accuracy)
            print(str(int(time_elapsed * 1000)) + ' ms')

    print("------------------------------------------------")
    print problem.__class__
    print 'overall win: ' + str(int(float(trueSum) / float(testNum) * 100)) + "%"
    print 'overall accuracy: ' + str(int(float(overallAccuracy) / float(testNum) * 100)) + "%"
    print 'overall time: ' + str(int((float(overallTime) / float(testNum)) * 1000)) + ' ms'
    print("------------------------------------------------")

args = sys.argv
if(args[2] == "NPuzzleProblem"):
    problem = NPuzzleProblem(int(args[3]))
elif(args[2] == "NQueenProblem"):
    problem = NQueenProblem(int(args[3]))


solve(int(args[1]), problem, len(args) == 5 and args[4] == "--trace")