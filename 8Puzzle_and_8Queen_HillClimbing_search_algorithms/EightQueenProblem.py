import random
import math
from copy import deepcopy

class EightQueenProblem:
    # queens = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
    queens = []
    queens_num = 4
    def __init__(self):
        self.generateRandomQueens()
        print(self.queens)

    def generateRandomQueens(self):
        for i in range(self.queens_num):
            exists = True
            while exists:
                exists = False

                # generate new state
                state = (random.randrange(self.queens_num), random.randrange(self.queens_num))

                # ignore the checking for the first queen
                if(len(self.queens) == 0):
                    self.queens.append(state)
                    break

                # check if the new state not exists in queens
                for queen in self.queens:
                    if state == queen:
                        exists = True
                        break

                if not exists:
                    self.queens.append(state)


    def attackedCellsHeuristic(self):
        board = [[0 for i in range(self.queens_num)] for j in range(self.queens_num)]
        for (x, y) in self.queens:

            for i in range(self.queens_num):
                board[i][y] = 1

            for i in range(self.queens_num):
                board[x][i] = 1

            i, j = x, y
            while i != 0 and j != 0:
                i = i - 1
                j = j - 1
                board[i][j] = 1

            i, j = x, y
            while i != self.queens_num - 1 and j != self.queens_num - 1:
                i = i + 1
                j = j + 1
                board[i][j] = 1

            i, j = x, y
            while i != 0 and j != self.queens_num - 1:
                i = i - 1
                j = j + 1
                board[i][j] = 1

            i, j = x, y
            while i != self.queens_num - 1 and j != 0:
                i = i + 1
                j = j - 1
                board[i][j] = 1

        h = 0
        for i in board:
            for j in i:
                h += j
        return math.pow(self.queens_num, 2) - h
        


    def move(self, queen, state):
        i, j = state
        next = EightQueenProblem()
        next.queens = deepcopy(self.queens)

        if((i, j) not in next.queens):
            path = [str(next.queens.index(queen)) + " -> " + str(state)]
            next.queens.insert(next.queens.index(queen), (i, j))
            next.queens.remove(queen)
        else:
            next.queens = []
            path = []
        return next, path

# 0 x 0 0
# 0 0 x 0
# 0 0 0 1
# 0 0 x 0

# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0

p = EightQueenProblem()
print(p.attackedCellsHeuristic())