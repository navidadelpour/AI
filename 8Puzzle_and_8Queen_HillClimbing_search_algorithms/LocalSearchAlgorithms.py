from NPuzzleProblem import NPuzzleProblem
from NQueenProblem import NQueenProblem
import random
import math
from pprint import pprint
import time
import sys

def hillClimbing(problem, hardrate):
    t0 = time.time()
    cost = 0
    optimalCost = None

    problem.generateRandomBoard(hardrate)
    initialH = problem.heuristic()
    current = (problem, initialH, [])
    
    while(True):
        successors = current[0].getSuccessors()
        successor = successors[0]
        if successor[1] >= current[1]:
            answer = current
            break
        current = (successor[0], successor[1], current[2] + successor[2])

    # calculate statistics
    time_elapsed = time.time() - t0
    accuracy = 1 - float(answer[1]) / float(initialH) if initialH and answer[1] else 1
    isGoal = answer[0].isGoal()
    cost = len(answer[2])
    if isGoal: optimalCost = cost 

    answer = answer + (isGoal, accuracy, problem, time_elapsed, cost, optimalCost)
    return answer

def simulatedAnnealing(problem, hardrate):
    t0 = time.time()
    cost = 0
    optimalCost = None

    temperature = 10000
    coolingRate = .003
    problem.generateRandomBoard(hardrate)
    initialH = problem.heuristic()
    current = (problem, initialH, [])
    answer = None

    while(temperature > 1):
        answer = current
        if(current[0].isGoal()):
            break

        successors = current[0].getSuccessors()
        successor = successors[random.randrange(len(successors))]

        if(probability(current[1], successor[1], temperature) > random.uniform(0, 1)):
            current = (successor[0], successor[1], current[2] + successor[2])

        temperature = temperature - temperature * coolingRate

    # calculate statistics
    time_elapsed = time.time() - t0
    accuracy = 1 - float(answer[1]) / float(initialH) if initialH and answer[1] else 1
    isGoal = answer[0].isGoal()
    cost = len(answer[2])
    if isGoal: optimalCost = cost 

    answer = answer + (isGoal, accuracy, problem, time_elapsed, cost, optimalCost)
    return answer

def probability(e1, e2, t):
    de = e2 - e1
    return 1 if de > 0 else math.exp(de / t)

def solve(testNum, problem, algorithm, trace):
    trueSum = 0
    overallAccuracy = 0
    overallTime = 0
    overallCost = 0
    hardrate = 20
    for i in range (testNum):
        if algorithm == 'hillClimbing':
            answer = hillClimbing(problem, hardrate)
        elif algorithm == 'simulatedAnnealing':
            answer = simulatedAnnealing(problem, hardrate)
        else:
            return
        solution, h, path, isGoal, accuracy, initialState, time_elapsed, cost, optimalCost = answer
        if(isGoal):
            trueSum += 1
        overallAccuracy += accuracy
        overallTime += time_elapsed
        overallCost += cost
        if(trace):
            print("------------------------------------------------")
            print("problem, h: \t\t" + str((initialState.getState(), initialState.heuristic())))
            print("solution, h: \t\t" + str((solution.getState(), solution.heuristic())))
            print("path: \t\t\t" + str(path))
            print("win: \t\t\t" + str(isGoal))
            print("cost: \t\t\t" + str(cost))
            print("optimal cost: \t\t" + str(optimalCost))
            print("accuracy: \t\t" + str('%.2f' % accuracy))
            print("time elapsed: \t\t" + str(int(time_elapsed * 1000)) + ' ms')

    print("------------------------------------------------")
    print "algorithm: \t\t" + str(algorithm)
    print "problem: \t\t" + str(problem.__class__.__name__)
    print 'overall win: \t\t' + str(int(float(trueSum) / float(testNum) * 100)) + "%"
    print 'overall accuracy: \t' + str(int(float(overallAccuracy) / float(testNum) * 100)) + "%"
    print 'overall time: \t\t' + str(int((float(overallTime) / float(testNum)) * 1000)) + ' ms'
    print 'overall cost: \t\t' + str((float(overallCost) / float(testNum)))
    print("------------------------------------------------")

args = sys.argv
if len(args) > 4:
    if(args[2] == "NPuzzleProblem"):
        problem = NPuzzleProblem(int(args[3]))
    elif(args[2] == "NQueenProblem"):
        problem = NQueenProblem(int(args[3]))

    solve(int(args[1]), problem, args[4], len(args) == 6 and args[5] == "--trace")
else:
    solve(12, NPuzzleProblem(8), "hillClimbing", "")
    solve(12, NPuzzleProblem(8), "simulatedAnnealing", "")

    solve(12, NQueenProblem(8), "hillClimbing", "")
    solve(12, NQueenProblem(8), "simulatedAnnealing", "")

