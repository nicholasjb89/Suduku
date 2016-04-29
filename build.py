import board
import random
import copy

FULLBOARD = board.buildBoard()
GAMEBOARD = copy.copy(FULLBOARD)
TEMPREMOVED = [0,0] # index, number
REMAINING = list(range(0,81))
REMOVED_INDEXES = []

def numberRemove():
    """removes a number from gameboard"""

    TEMPREMOVED[0] = random.choice(REMAINING)
    TEMPREMOVED[1] = FULLBOARD[TEMPREMOVED[0]]
    REMAINING.remove(TEMPREMOVED[0])
    REMOVED_INDEXES.append(TEMPREMOVED[0])
    GAMEBOARD[TEMPREMOVED[0]] = 0 # replace the number with an empty string


def undoRemove():
    """undo's the remove"""
    global TEMPREMOVED

    REMAINING.append(TEMPREMOVED[0])
    GAMEBOARD[TEMPREMOVED[0]] = TEMPREMOVED[1]
    REMOVED_INDEXES.remove(TEMPREMOVED[0])
    TEMPREMOVED = [0,0] # reset tempremove


def solvable():
    """returns true if it is solvable"""
    tempBoard = copy.copy(GAMEBOARD)
    tempRemoved = copy.copy(REMOVED_INDEXES)
    f_solvable = False

    while True:
        for index in REMOVED_INDEXES:
            col = board.getColNumbers(index,tempBoard)
            row = board.getRowNumbers(index,tempBoard)
            square = board.getSquareNumbers(index,tempBoard)

            validNumbers = []
            for n in col:
                if n in row and n in square:
                    validNumbers.append(n)

            if len(validNumbers) == 1:
                tempBoard[index] == validNumbers[0]
                tempRemoved.remove(index)
                f_solvable = True

        if f_solvable == False:
            return False
        elif len(tempRemoved) == 0:
            return True

        f_solvable = False

#remove random numbers

numberRemove()
numberRemove()
numberRemove()
numberRemove()
numberRemove()
numberRemove()
numberRemove()
numberRemove()

while True:
    row = []
    index = 0
    for num in GAMEBOARD:
        row.append(num)
        if index == 8:
            print(row)
            row = []
            index = -1

        index += 1
    break

print(solvable())





















