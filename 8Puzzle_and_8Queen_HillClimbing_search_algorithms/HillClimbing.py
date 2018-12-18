from Problem import EightPuzzleProblem;
import random;

def hillClimbing(problem):
    problem.generateRandomBoard()
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


testNum = 100
trueSum = 0
midAccuracy = 0

for i in range (testNum):
    solution, h, path, isGoal, accuracy, initialState = hillClimbing(EightPuzzleProblem())
    if(isGoal):
        trueSum += 1
        print("startState", initialState.board, initialState.manhatanHeuristic())
        print("solution", solution.board, solution.manhatanHeuristic())
        print(path)
    print(isGoal, accuracy)
    midAccuracy += accuracy

print trueSum * .01
print midAccuracy / testNum