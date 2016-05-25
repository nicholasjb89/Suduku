import random
import copy

def isBoard(board):
    """
    Test to see if it is a legit board or not
    Will not test to see if it is solvable just make sure its a board that can
    run thought the solver
    :param board:
    :return: Bool
    """
    if type(board) != type(list()):
        print(type(board), type(list()))
        return False
    elif len(board) != 81:
        print(len(board))
        return False
    for n in board:
        if n not in range(0,10):
            return False

    return True


def textToBoard(path):
    """
    :param path:
    :return: 2 Dim list that is all the boards in the text file
    """
    file = open(path, mode="r")

    all = []
    for line in file:
        board = []
        for char in line:
            if char == ".":
                board.append(0)
            else:
                try:
                    board.append(int(char))
                except:
                    continue
        if board != []:
            all.append(board)

    file.close()

    return all

def displayBoard(board, header = ""):
    print()
    print(header)
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

def compare(board1,board2):
    """
    :param board1: Board list
    :param board2: Board list
    :return: Void
    """

    different = []

    for i in range(len(board1)):
        if board1[i] == board2[i]:
            different.append(" ")
        else:
            different.append(board1[i])

    displayBoard(different)

class Validate():
    def __init__(self, boardClass):
        self.Board = boardClass

    def isRepeated(self, number, indexes, board):
        count = 0
        for i in indexes:
            if number == board[i]:
                count += 1

        if count > 1:
            return True
        else:
            return False

    def validateBoard(self, board):
        f_missingIndex = False
        missingIndexPositions = []
        f_repeatedNumber = False
        repeatedNumbers = []
        for i in range(0,81):
            n = board[i]
            indexNumPair = (i,n)
            row = self.Board.getRowIndexes(i)
            col = self.Board.getColIndexes(i)
            square = self.Board.getSquareIndexes(i)
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

        if f_repeatedNumber or f_missingIndex:
            return False
        else:
            return True

class Solve():
    def __init__(self,boardClass):
        self.Board = boardClass

    def findMostValuableIndexes(self,board,adjust2):
        """
        This will look at the board and try to find what indexes are the most valuable.
        Valuable will ve if a number is put in that index more of the board will be solvable
        Also cant have too many pssable numbers for each valuable number index. i would say 3 max though this is
        semi random number.
        :param board: board list
        :return: list of most valuableindexes
        """
        two = []
        three = []
        valuableIndexes = []
        for index in self.Board.getMissingIndexes(board):
            possableNumbers = self.getValidNumbers(index,board)
            if len(possableNumbers) == 3:
                three.append(index)
            elif len(possableNumbers) == 2:
                two.append(index)

        for index in two:
            if len(valuableIndexes) != adjust2:
                valuableIndexes.append(index)
            else:
                return valuableIndexes

        remaining = adjust2-len(valuableIndexes)

        for i in range(0,remaining):
            try:
                valuableIndexes.append(three[i])
            except:
                break

        return valuableIndexes

    def getValidNumbers(self, index, board):
        numbers = []
        square = self.Board.getSquareNumbers(index,board)
        row = self.Board.getRowNumbers(index,board)
        col = self.Board.getColNumbers(index,board)

        for n in square:
            if n in row and n in col:
                numbers.append(n)

        return numbers

    def alg1(self, board):
        missingIndexes = self.Board.getMissingIndexes(board)

        f_solvable = False
        while True:
            for index in missingIndexes:
                validNumbers = self.getValidNumbers(index, board)
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
        missingIndexes = self.Board.getMissingIndexes(board)

        f_solvable = False
        while True:

            for index in missingIndexes:

                squareIndexes = self.Board.getSquareIndexes(index)
                squareMissingIndexes = []

                #find all the missing indexed ins the square
                for i in squareIndexes:
                    if board[i] == 0:
                        squareMissingIndexes.append(i)

                #find all the possable numbers that could go in this index
                validNumbers = self.getValidNumbers(index, board)

                #loop through all the numbers to see if we can elimenate all but one index for the number
                for n in validNumbers:
                    tempBoard = copy.copy(board)
                    for i in squareMissingIndexes:
                        if n not in self.Board.getRowNumbers(i,board) or n not in self.Board.getColNumbers(i,board):
                            if i != index:
                                tempBoard[i] = n

                    missing = 0
                    for i in self.Board.getSquareIndexes(i):
                        if tempBoard[i] == 0:
                            missing += 1
                    if missing == 1:

                        board[index] = n
                        missingIndexes = self.Board.getMissingIndexes(board)
                        f_solvable = True
                        break
            if f_solvable == False or len(missingIndexes) == 0:
                return board

            f_solvable = False
        return board

    def charleyAlg(self,board):
        """this is charleys brute force alg"""
        for i in self.Board.getMissingIndexes(board):
            validNumbers = self.getValidNumbers(i, board)

            try:
                board[i] = random.choice(validNumbers)
            except:
                break

        return board

    def solve(self,board, useCharleyAlg = True,adjust1 = 10, adjust2 = 10):
        board = self.alg1(board)
        board = self.alg2(board)
        if not useCharleyAlg:
            return board

        bestBoard = board
        "This is the Game Board before Brute Force"
        if self.Board.validate.validate(board):
            return board
        else:
            i = 0
            valuedIndexes = self.findMostValuableIndexes(board,adjust1)
            seedBoard = copy.copy(board)
            for index in valuedIndexes:
                try:
                    seedBoard[index] = random.choice(self.getValidNumbers(index,seedBoard))
                except:
                    continue

            tempBoard = copy.copy(seedBoard)
            tempBoard = self.alg1(tempBoard)
            tempBoard = self.alg2(tempBoard)
            while True:
                i += 1

                tempBoard = self.charleyAlg(tempBoard)
                if len(self.Board.getMissingIndexes(tempBoard)) < len(self.Board.getMissingIndexes(bestBoard)):
                    bestBoard = tempBoard
                if i%adjust2 == 0:
                    seedBoard = copy.copy(board)
                    for index in valuedIndexes:
                        try:
                            seedBoard[index] = random.choice(self.getValidNumbers(index,seedBoard))
                        except:
                            continue

                    tempBoard = copy.copy(seedBoard)
                    tempBoard = self.alg1(tempBoard)
                    tempBoard = self.alg2(tempBoard)

                if i == 20000:
                    # if there are more than 10K attempts stop trying to solve and return False
                    print("after 20000 attempts it could not be solved")
                    return bestBoard

                if self.Board.validate.validate(tempBoard):
                    print("Charley Alg Total Attempts = ", i)
                    return tempBoard

class Board():
    def __init__(self, solveClass = Solve, validateClass = Validate):
        self.solver = solveClass(self)
        self.validate = validateClass(self)

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

    def getMissingIndexes(self,theList):
        """
        :param theList: could be an single dim list. could use a square, row, col, or board
        :return: all the Zeros in the given list
        """
        indexes = []
        for i in range(0,len(theList)):
            if theList[i] == 0:
                indexes.append(i)
        return indexes

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

    def attemptBuild(self):
        self.solvedBoard = [0] * 81
        for i in range(81):
            tempBoard = self.getSolvedBoard()
            rowNums = self.getRowNumbers(i, tempBoard)
            colNums = self.getColNumbers(i, tempBoard)
            squareNums = self.getSquareNumbers(i, tempBoard)

            validNumbers = []

            for n in rowNums:
                if n in colNums and n in squareNums:
                    validNumbers.append(n)
            try:
                self.solvedBoard[i] = random.choice(validNumbers)

            except:
                break

    def makeSolvableBoard(self, totalRemoved = 40):
        """ takes a full board anc makes a board for players to solve """
        board = self.getSolvedBoard()
        while totalRemoved != 0:
            indexes = list(range(0,81))
            rIndex = random.choice(indexes)
            tempBoard = copy.copy(board)
            tempBoard[rIndex] = 0
            if self.solver.solve(tempBoard, useCharleyAlg=False):
                board[rIndex] = 0
                totalRemoved -= 1
        self.board = board

    def build(self):
        self.failed = 0
        while True:
            self.attemptBuild()
            if self.validate.validate(self.solvedBoard):
                break
            self.failed += 1

        self.makeSolvableBoard()

    def getSolvedBoard(self):
        return copy.copy(self.solvedBoard)

    def getBoard(self):
        return copy.copy(self.board)