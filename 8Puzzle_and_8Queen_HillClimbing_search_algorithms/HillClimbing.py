from Problem import EightPuzzleProblem;
from Queue import Queue;


def hillClimbing(problem):
    current = (problem, [])
    while(True):
        currentH = current[0].manhatanHeuristic()
        bestSuccessor = current[0].getBestSuccessors()
        bestSuccessorH = bestSuccessor[0].manhatanHeuristic()

        if bestSuccessorH < currentH:
            answer = (bestSuccessor[0], current[1] + bestSuccessor[1])
            break
        current = (bestSuccessor[0], current[1] + bestSuccessor[1])

        
    isGoal = answer[0].board == problem.goal
    answer = answer + (isGoal, )
    return answer

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



# (<Problem.EightPuzzleProblem instance at 0x0000000002AE1A48>, 13.0, 'right', False)
# answers = hillClimbing2(EightPuzzleProblem())
# print("end")
# print(answers)

# solution, h, path, isGoal = hillClimbing2(EightPuzzleProblem())
# print("--------------------------------------------------------------------------------")
# print(solution.board)
# print(h)
# print(path)
# print(isGoal)
# print("--------------------------------------------------------------------------------")
