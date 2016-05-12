import random
import copy

def displayBoard(board):
    print()
    row = []
    col = 1
    for n in board:
        if len(row) != 9:
            row.append(n)
        elif len(row) == 9:
            for i in range(0,9):
                if i%3 == 0:
                    print(" |",end="")
                print(row[i], end=" ")
            row = []
            row.append(n)
            print()
            if col %3 == 0:
                print(" -----------------------")
            col += 1
    for i in range(0,9):
        if i%3 == 0:
            print(" |",end="")
        print(row[i], end=" ")
    print()

class Validate():
    def getSquareIndexes(self,index):
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
                    indexes.append(i)
        return indexes

    def getRowIndexes(self, index):
        indexes = []

        offset = index%9
        index -= offset

        for i in range(index,index+9):
            indexes.append(i)

        return indexes

    def getColIndexes(self,index):
        indexes = []
        while True:
        #start at the begining of the collumn
            if index - 9 >= 0:
                index -= 9
            else:
                break
        while True:
            indexes.append(index)
            index += 9

            if index >= 81:
                break

        return indexes

    def isRepeated(self, number, indexes, board):
        count = 0
        for i in indexes:
            if number == board[i]:
                count += 1

        if count > 1:
            return True
        else:
            return False

    def validateBoard(self,board):
        f_missingIndex = False
        missingIndexPositions = []
        f_repeatedNumber = False
        repeatedNumbers = []
        for i in range(0,81):
            n = board[i]
            indexNumPair = (i,n)
            row = self.getRowIndexes(i)
            col = self.getColIndexes(i)
            square = self.getSquareIndexes(i)
            if n == 0:
                f_missingIndex = True
                missingIndexPositions.append(i)

            if self.isRepeated(n, row, board):
                f_repeatedNumber = True
                if indexNumPair not in repeatedNumbers:
                    repeatedNumbers.append(indexNumPair)
            if self.isRepeated(n, col, board):
                f_repeatedNumber = True
                if indexNumPair not in repeatedNumbers:
                    repeatedNumbers.append(indexNumPair)
            if self.isRepeated(n, square, board):
                f_repeatedNumber = True
                if indexNumPair not in repeatedNumbers:
                    repeatedNumbers.append(indexNumPair)

        return f_missingIndex, missingIndexPositions, f_repeatedNumber, repeatedNumbers

    def validate(self,board, errorLog = False):
        f_missingIndex, missingIndexPositions, f_repeatedNumber, repeatedNumbers = self.validateBoard(board)

        if f_missingIndex and errorLog:
            print("There are missing boxes in the board at these positions")
            print(missingIndexPositions)
        if f_repeatedNumber and errorLog:
            print()
            print("There are repeated numbers in the board")
            failBoard = []
            rIndex = 0

            for i in range(0,81):
                if rIndex < len(repeatedNumbers):
                    if i == repeatedNumbers[rIndex][0]:
                        failBoard.append(repeatedNumbers[rIndex][1])
                        rIndex += 1
                    else:
                        failBoard.append(" ")
                else:
                        failBoard.append(" ")
            displayBoard(failBoard)

        if f_repeatedNumber or f_missingIndex:
            return False
        else:
            return True

class Solve():
    def __init__(self,validateClass):
        self.validate = validateClass

    def alg1(self, board):
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

    def alg2(self,board):
        pass

    def charleyAlg(self,board):
        """this is charleys brute force alg"""

        for i in self.getMissingIndexes(board):
            row = self.getRowNumbers(i,board)
            col = self.getColNumbers(i,board)
            square = self.getSquareNumbers(i,board)
            validNumbers = []
            for n in row:
                if n in col and n in square:
                    validNumbers.append(n)
            try:
                board[i] = random.choice(validNumbers)
            except:
                break

        return board

    def solve(self,board):
        board = self.alg1(board)
        bestBoard = board
        "This is the Game Board before Brute Force"
        if Validate().validate(board):
            return board
        else:
            i = 0
            while True:
                i += 1
                tempBoard = self.charleyAlg(copy.copy(board))
                if len(self.getMissingIndexes(tempBoard)) < len(self.getMissingIndexes(bestBoard)):
                    bestBoard = tempBoard

                if(i%1000 == 0):
                    print("attempts made: ",  i)
                    displayBoard(bestBoard)
                if Validate().validate(tempBoard):
                    return tempBoard

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
            if index - 9 >= 0:
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

        for square in squareIndexes:
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

class Board():
    def __init__(self, solveClass, validateClass):
        self.solver = solveClass(validateClass)
        self.validate = validateClass()
        self.build()

    def attemptBuild(self):
        self.board = [0] * 81
        for i in range(81):
            tempBoard = self.getBoard()
            rowNums = self.solver.getRowNumbers(i, tempBoard)
            colNums = self.solver.getColNumbers(i, tempBoard)
            squareNums = self.solver.getSquareNumbers(i, tempBoard)

            validNumbers = []

            for n in rowNums:
                if n in colNums and n in squareNums:
                    validNumbers.append(n)
            try:
                self.board[i] = random.choice(validNumbers)

            except:
                break

    def build(self):
        self.failed = 0
        while True:
            self.attemptBuild()
            if self.validate.validate(self.board):
                break
            self.failed += 1

    def getBoard(self):
        return copy.copy(self.board)



