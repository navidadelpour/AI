from Problem import EightPuzzleProblem;
from Queue import Queue;


def hillClimbing(problem):
    problem.generateRandomBoard()
    initialH = problem.manhatanHeuristic()
    current = (problem, initialH,[])
    while(True):
        bestSuccessor = current[0].getBestSuccessors()[0]
        if bestSuccessor[1] >= current[1]:
            answer = current
            break
        current = (bestSuccessor[0], bestSuccessor[1], current[2] + bestSuccessor[2])

        
    if initialH:
        accuracy = current[1] / initialH
    else:
        accuracy = "infinite"
    isGoal = answer[0].board == problem.goal

    answer = answer + (isGoal, accuracy, problem)
    return answer


#not usefull
def hillClimbing2(problem):
    current = (problem, [])
    answers = []
    stack = []
    stack.append((problem, problem.manhatanHeuristic(), [], False))
    i = 0
    print('start')
    while(True):
        print('---------------stack-------------------')
        for x in stack:
            print (x[0].board, x[1])
        print('-----------------------------------------')
        current = stack.pop()
        bestSuccessors = current[0].getBestSuccessors()

        print(current[0].board, current[1])
        print('successors')
        for b in bestSuccessors:
            print(b[0].board, b[1])
        if(bestSuccessors[0][1] < current[1]):
            stack = stack + bestSuccessors
        else:
            answers.append(current)
        i += 1
        if i > 4:
            break        



# answers = hillClimbing2(EightPuzzleProblem())
# print("end")
# print(answers)
k = 0
for i in range (100):
    solution, h, path, isGoal, accuracy, initialState = hillClimbing(EightPuzzleProblem())
    # print("--------------------------------------------------------------------------------")
    # print("startState", initialState.board, initialState.manhatanHeuristic())
    # print("solution", solution.board, solution.manhatanHeuristic())
    # print(path)
    if(isGoal):
        k += 1
        print("startState", initialState.board, initialState.manhatanHeuristic())
        print("solution", solution.board, solution.manhatanHeuristic())
        print(path)

    print(isGoal, accuracy)
    # print(accuracy)
    # print("--------------------------------------------------------------------------------")
print k