from Problem import EightPuzzleProblem;

def hillClimbing(problem):
    current = (problem, [])
    while(True):
        currentH = current[0].manhatanHeuristic()
        bestSuccessor = current[0].getBestSuccessor()
        bestSuccessorH = bestSuccessor[0].manhatanHeuristic()

        if bestSuccessorH >= currentH or bestSuccessorH == 0:
            answer = (bestSuccessor[0], current[1] + bestSuccessor[1])
            break
        current = (bestSuccessor[0], current[1] + bestSuccessor[1])
    isGoal = answer[0].board == problem.goal
    answer = answer + (isGoal, )
    return answer
solution, path, isGoal = hillClimbing(EightPuzzleProblem())
print("--------------------------------------------------------------------------------")
print(solution.board)
print(path)
print(isGoal)
print("--------------------------------------------------------------------------------")
