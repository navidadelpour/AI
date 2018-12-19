import random

class EightQueenProblem:
    queens = []

    def __init__(self):
        self.generateRandomQueens()

    def generateRandomQueens(self):
        for i in range(8):
            exists = True
            while exists:
                exists = False

                # generate new state
                state = (random.randrange(8), random.randrange(8))

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


EightQueenProblem()