from Problem import EightPuzzleProblem;

def hillClimbing(problem):
    current = problem
    while(True):
        currentH = problem.manhatanHeuristic()
        bestSuccessor = current.getBestSuccessor()
        bestSuccessorH = bestSuccessor.manhatanHeuristic()

        if bestSuccessorH >= currentH or bestSuccessorH == 0:
            return bestSuccessor
        current = bestSuccessor
        
    
x = hillClimbing(EightPuzzleProblem())

print(x.board)