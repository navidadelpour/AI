from Problem import EightPuzzleProblem;

def hillClimbingNextMove(problem):
    current = problem.getIndex(problem.board, 0)
    currentH = problem.manhatanHeuristic()

    bestSuccessor = problem.getBestSuccessor()
    bestSuccessorH = bestSuccessor.manhatanHeuristic()

    if currentH >= bestSuccessorH:
        return problem
    else:
        return bestSuccessor
    

hillClimbingNextMove(EightPuzzleProblem())