import random;
import copy;
from enum import Enum;

class Directions(Enum):
    up = 1,
    down = 2,
    left = 3,
    right = 4

class EightPuzzleProblem:

    goal = []
    board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

    def __init__(self):
        self.setGoal()

    def setBoard(self, board):
        self.board = board
    
    def setGoal(self):
        value = 1
        for i in range(3):
            temp = []
            for j in range(3):
                if(value == 9):
                    value = 0
                temp.append(value)
                value += 1
            self.goal.append(temp)  

    # getting the best successor for a given problem
    def getBestSuccessor(self):
        bestSuccessor = []
        blockDirections = self.getBlockDirections(self.getIndex(self.board, 0))
        
        for direction in Directions:
            successor = EightPuzzleProblem()
            successor.setBoard(self.move(direction))
            if len(successor.board) > 0:
                successorH = successor.manhatanHeuristic()
                if len(bestSuccessor) == 0 or bestSuccessor[1] < successorH:
                    bestSuccessor = (successor, successorH)
        
        return bestSuccessor[0]
        
    def move(self, direction):
        x, y = self.getIndex(self.board, 0)

        blockDirections = self.getBlockDirections((x, y))
        # checking the what directions are blocked
        if direction in blockDirections:
            return []

        # calculate next position after doing directions
        x2, y2 = self.getTargetState((x, y), direction)

        # swap
        nextBoard = copy.deepcopy(self.board)
        target = nextBoard[x2][y2]
        nextBoard[x2][y2] = 0
        nextBoard[x][y] = target

        return nextBoard

    # calculating block directions of a given state
    def getBlockDirections(self, state):
        x, y = state
        blockDirections = []
        if x == 0:
            blockDirections.append(Directions.up)
        elif x == 2:
            blockDirections.append(Directions.down)
        elif y == 0:
            blockDirections.append(Directions.left)
        elif y == 2:
            blockDirections.append(Directions.right)
        
        return blockDirections

    # calculate target state after a given state move towards a given direction
    def getTargetState(self, state, direction):
        x, y = state
        if(direction == Directions.up):
            x2, y2 = x - 1, y
        elif(direction == Directions.down):
            x2, y2 = x + 1, y
        elif(direction == Directions.left):
            x2, y2 = x, y - 1
        elif(direction == Directions.right):
            x2, y2 = x, y + 1
        
        return (x2, y2)

    def getIndex(self, board,value):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if board[i][j] == value:
                    return (i, j)
    
    def manhatanHeuristic(self):
        h = 0
        for k in range(1, 9):
            x1, y1 = self.getIndex(self.board, k)
            x2, y2 = self.getIndex(self.goal, k)

            h += x2 - x1 + y2 - y1
        return h

#porblem = EightPuzzleProblem()
