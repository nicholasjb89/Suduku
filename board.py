import random
import copy

def getSquareIndexes(index,board):
    squareIndexes = (0,1,2,9,10,11,18,19,20),\
                    (3,4,5,12,13,14,21,22,23),\
                    (6,7,8,15,16,17,24,25,26),\
                    (27,28,29,36,37,38,45,46,47),\
                    (30,31,32,39,40,41,48,49,50),\
                    (33,34,35,42,43,44,51,52,53),\
                    (54,55,56,63,64,65,72,73,74),\
                    (57,58,59,66,67,68,75,76,77),\
                    (60,61,62,69,70,71,78,79,80)
    indexes = []
    for square in squareIndexes:
        if index in square:
            for i in square:
                if board[index] == 0:
                    indexes.append(i)
    return indexes

def getRowIndexes(index,board):
    indexes = []

    offset = index%9
    index -= offset

    for i in range(index,index+9):
        if board[i] == 0:
            indexes.append(i)

    return indexes

def getColIndexes(index,board):
    indexes = []
    while True:
    #start at the begining of the collumn
        if index - 9 > 0:
            index -= 9
        else:
            break
    while True:
        if board[index] == 0:
            indexes.append(index)
        index += 9
        if index >=81:
            break

    return indexes

class Solve():
    def __init__(self):
        pass

    def solve(self,board):
        missingIndexes = self.getMissingIndexes(board)

        f_solvable = False
        while True:
            for index in missingIndexes:
                col = self.getColNumbers(index, board)
                row = self.getRowNumbers(index, board)
                square = self.getSquareNumbers(index, board)

                validNumbers = []
                for n in col:
                    if n in row and n in square:
                        validNumbers.append(n)
                if len(validNumbers) == 1:
                    board[index] = validNumbers[0]
                    missingIndexes.remove(index)
                    f_solvable = True

            if f_solvable == False:
                return board
            elif len(missingIndexes) == 0:
                return board

            f_solvable = False

    def getRowNumbers(self, index, board):
        validNumbers = list(range(1,10))

        offset = index%9
        index -= offset

        for i in range(index,index+9):
            if board[i] != 0:
                validNumbers.remove(board[i])

        return validNumbers

    def getColNumbers(self,index, board):
        validNumbers = list(range(1,10))

        while True:
            #start at the begining of the collumn
            if index - 9 > 0:
                index -= 9
            else:
                break

        while True:
            #find the numbers in that collumn and remove them from validNumbers
            if board[index] != 0:
                validNumbers.remove(board[index])
            index += 9
            if index >=81:
                break

        return validNumbers

    def getSquareNumbers(self,index,board):
        validNumbers = list(range(1,10))
        squareIndexes = (0,1,2,9,10,11,18,19,20),\
                        (3,4,5,12,13,14,21,22,23),\
                        (6,7,8,15,16,17,24,25,26),\
                        (27,28,29,36,37,38,45,46,47),\
                        (30,31,32,39,40,41,48,49,50),\
                        (33,34,35,42,43,44,51,52,53),\
                        (54,55,56,63,64,65,72,73,74),\
                        (57,58,59,66,67,68,75,76,77),\
                        (60,61,62,69,70,71,78,79,80)

        for square  in squareIndexes:
            if index in square:
                break

        for index in square:
            if board[index] != 0:
                validNumbers.remove(board[index])

        return validNumbers

    def getMissingIndexes(self,board):
        indexes = []
        for i in range(0,81):
            if board[i] == 0:
                indexes.append(i)
        return indexes

    def isValid(self, board):
        if 0 in board:
            return False
        else:
            return True

class Board():
    def __init__(self, solveClass):
        self.solve = solveClass()
        self.build()

    def attemptBuild(self):
        self.board = [0] * 81
        for i in range(81):
            tempBoard = self.getBoard()
            rowNums = self.solve.getRowNumbers(i, tempBoard)
            colNums = self.solve.getColNumbers(i, tempBoard)
            squareNums = self.solve.getSquareNumbers(i, tempBoard)

            validNumbers = []

            for n in rowNums:
                if n in colNums and n in squareNums:
                    validNumbers.append(n)
            try:
                self.board[i] = random.choice(validNumbers)

            except:
                break

    def build(self):
        while True:
            self.attemptBuild()
            if self.solve.isValid(self.board):
                break

    def getBoard(self):
        return copy.copy(self.board)

if __name__ == "main":
    pass




