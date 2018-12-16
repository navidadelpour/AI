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


    def move(self, direction):
        x, y = self.getIndex(self.board, 0)

        # checking the what directions are blocked
        blockDirections = []
        if x == 0:
            blockDirections.append(Directions.up)
        elif x == 2:
            blockDirections.append(Directions.down)
        elif y == 0:
            blockDirections.append(Directions.left)
        elif y == 2:
            blockDirections.append(Directions.right)
        
        if direction in blockDirections:
            return False
        
        # calculate next position after doing directions
        if(direction == Directions.up):
            x2, y2 = x - 1, y
        elif(direction == Directions.down):
            x2, y2 = x + 1, y
        elif(direction == Directions.left):
            x2, y2 = x, y - 1
        elif(direction == Directions.right):
            x2, y2 = x, y + 1

        # swap
        return_board = copy.deepcopy(self.board)
        target = return_board[x2][y2]
        return_board[x2][y2] = 0
        return_board[x][y] = target

        return return_board

    def getIndex(self, board,value):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if board[i][j] == value:
                    return (i, j)
    
    def manhatanHeuristic(self):
        return_value = 0
        for k in (range(9) + 1):
            x1, y1 = self.getIndex(self.board, k)
            x2, y2 = self.getIndex(self.goal, k)

            return_value += x2 - x1 + y2 - y1
        return return_value
        
porblem = EightPuzzleProblem()
