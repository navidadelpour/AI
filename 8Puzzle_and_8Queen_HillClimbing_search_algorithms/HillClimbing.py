from EightPuzzleProblem import EightPuzzleProblem
import random
import math

def hillClimbing(problem, hardrate):
    problem.generateRandomBoard(hardrate)
    initialH = problem.manhatanHeuristic()
    current = (problem, initialH,[])

    while(True):
        bestSuccessors = current[0].getBestSuccessors()
        bestSuccessor = bestSuccessors[0]
        if bestSuccessor[1] >= current[1]:
            answer = current
            break
        current = (bestSuccessor[0], bestSuccessor[1], current[2] + bestSuccessor[2])

    accuracy = current[1] / initialH if initialH else 1
    isGoal = answer[0].board == problem.goal

    answer = answer + (isGoal, accuracy, problem)
    return answer


def eightPuzzleProblemWithHillClimbing():
    testNum = 100
    trueSum = 0
    midAccuracy = 0
    hardrate = 10

    for i in range (testNum):
        problem = EightPuzzleProblem()
        solution, h, path, isGoal, accuracy, initialState = hillClimbing(problem, hardrate)
        if(isGoal):
            trueSum += 1
        midAccuracy += accuracy

    print 'win rate: ' + str(float(trueSum) / float(testNum))
    print 'accuracy rate: ' + str(1 - (float(midAccuracy) / float(testNum)))

eightPuzzleProblemWithHillClimbing()