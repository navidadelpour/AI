import random
import math
from copy import deepcopy, copy
from pprint import pprint

class NQueenProblem:

    queens = []
    queens_num = 8

    def __init__(self, n):
        self.queens_num = n

    def getState(self):
        return self.queens

    def isGoal(self):
        return self.heuristic() == 0

    def generateRandomBoard(self, hardrate):
        self.queens = []
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


    # conflict heuristic
    def heuristic(self):
        qs = deepcopy(self.queens)

        for (x, y) in self.queens:
            for i in range(self.queens_num):
                if (i, y) in qs and (i, y) != (x, y):
                    qs.remove((i, y)) 

            for i in range(self.queens_num):
                if (x, i) in qs and (x, i) != (x, y):
                    qs.remove((x, i)) 

            # simpler version of the code below
            for k in range(4):
                i, j = x, y
                di, dj, condition = self.getStep(i, j, k)
                while condition:
                    condition = (self.getStep(i, j, k))[2]
                    i += di
                    j += dj
                    if (i, j) in qs and (i, j) != (x, y):
                        qs.remove((i, j))

            # i, j = x, y
            # while i != 0 and j != 0:
            #     i = i - 1
            #     j = j - 1
            #     board[i][j] = 1
            #     if (i, j) in qs and (i, j) != (x, y):
            #         qs.remove((i, j)) 

            # i, j = x, y
            # while i != 0 and j != self.queens_num - 1:
            #     i = i - 1
            #     j = j + 1
            #     board[i][j] = 1
            #     if (i, j) in qs and (i, j) != (x, y): 
            #         qs.remove((i, j)) 

            # i, j = x, y
            # while i != self.queens_num - 1 and j != 0:
            #     i = i + 1
            #     j = j - 1
            #     board[i][j] = 1
            #     if (i, j) in qs and (i, j) != (x, y):
            #         qs.remove((i, j)) 

            # i, j = x, y
            # while i != self.queens_num - 1 and j != self.queens_num - 1:
            #     i = i + 1
            #     j = j + 1
            #     board[i][j] = 1
            #     if (i, j) in qs and (i, j) != (x, y):
            #         qs.remove((i, j)) 

        return self.queens_num - len(qs)
        
    # used in heuristic function
    def getStep(self, i, j, k):
        if k == 0:
            return (-1, -1, i != 0 and j != 0)
        elif k == 1:
            return (-1, 1, i != 0 and j != self.queens_num - 1)
        elif k == 2:
            return (1, -1, i != self.queens_num - 1 and j != 0)
        elif k == 3:
            return(1, 1, i != self.queens_num - 1 and j != self.queens_num - 1)

    def getBestSuccessors(self):
        bestSuccessorsForQueens = []

        for queen in self.queens:
            bestSuccessors = []
            for i in range(self.queens_num):
                for j in range(self.queens_num):
                    successor, path = self.move(queen, (i, j))
                    h = successor.heuristic()
                    if len(successor.queens) != 0 :
                        bestSuccessors.append((successor, h, path))
            bestSuccessorsForQueens += bestSuccessors
        bestSuccessorsForQueens = sorted(bestSuccessorsForQueens, key = lambda x: x[1])
        maxH = bestSuccessorsForQueens[0][1]
        for b in copy(bestSuccessorsForQueens):
            if b[1] > maxH:
                bestSuccessorsForQueens.remove(b)
        return bestSuccessorsForQueens

    def move(self, queen, state):
        i, j = state
        next = NQueenProblem(self.queens_num)
        next.queens = deepcopy(self.queens)

        if((i, j) not in next.queens):
            path = [str(next.queens.index(queen)) + " in " + str(queen) + " -> " + str(state)]
            next.queens.insert(next.queens.index(queen), (i, j))
            next.queens.remove(queen)
        else:
            next.queens = []
            path = []
        return next, path