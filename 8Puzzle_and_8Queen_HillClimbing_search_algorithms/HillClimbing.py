from EightPuzzleProblem import EightPuzzleProblem
from EightQueenProblem import EightQueenProblem
import random
import math
from pprint import pprint

def hillClimbing(problem, hardrate):
    problem.generateRandomBoard(hardrate)
    initialH = problem.heuristic()
    current = (problem, initialH,[])

    while(True):
        bestSuccessors = current[0].getBestSuccessors()
        bestSuccessor = bestSuccessors[0]
        if bestSuccessor[1] >= current[1]:
            answer = current
            break
        current = (bestSuccessor[0], bestSuccessor[1], current[2] + bestSuccessor[2])

    accuracy = 1 - float(answer[1]) / float(initialH) if initialH and answer[1] else 1
    isGoal = answer[0].isGoal()

    answer = answer + (isGoal, accuracy, problem)
    return answer

def solve(problem):
    testNum = 10
    trueSum = 0
    midAccuracy = 0
    hardrate = 20
    for i in range (testNum):
        solution, h, path, isGoal, accuracy, initialState = hillClimbing(problem, hardrate)
        if(isGoal):
            trueSum += 1
        midAccuracy += accuracy
        # print("------------------------------------------------")
        # print(initialState.getState(), initialState.heuristic())
        # print(solution.getState(), solution.heuristic())
        # print(path)
        # print(isGoal)
        # print(accuracy)

    print("------------------------------------------------")
    print problem.__class__
    print 'win rate: ' + str(float(trueSum) / float(testNum))
    print 'accuracy rate: ' + str(float(midAccuracy) / float(testNum))
    print("------------------------------------------------")

solve(EightPuzzleProblem())
solve(EightQueenProblem())