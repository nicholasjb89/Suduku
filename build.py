import board
import random
import copy

def numberRemove(tempRemoved, remaining, removedIndexes, gameBoard):
    """removes a number from gameboard"""
    tempRemoved[0] = random.choice(remaining)
    tempRemoved[1] = gameBoard[tempRemoved[0]]
    remaining.remove(tempRemoved[0])
    removedIndexes.append(tempRemoved[0])
    gameBoard[tempRemoved[0]] = 0 # replace the number with an empty string

    return tempRemoved


def undoRemove(tempRemoved, remaining, removedIndexes, gameboard):
    """undo's the remove"""
    remaining.append(tempRemoved[0])
    gameboard[tempRemoved[0]] = tempRemoved[1]
    removedIndexes.remove(tempRemoved[0])

def solvable(gameBoard, removedIndexes):
    """returns true if it is solvable"""
    tempBoard = copy.copy(gameBoard)
    tempRemoved = copy.copy(removedIndexes)
    f_solvable = False

    while True:
        for index in tempRemoved:
            col = board.getColNumbers(index,tempBoard)
            row = board.getRowNumbers(index,tempBoard)
            square = board.getSquareNumbers(index,tempBoard)

            validNumbers = []
            for n in col:
                if n in row and n in square:
                    validNumbers.append(n)
            print(index,validNumbers)
            if len(validNumbers) == 1:

                tempBoard[index] == validNumbers[0]
                tempRemoved.remove(index)
                f_solvable = True

        if f_solvable == False:
            print(tempBoard)
            return False
        elif len(tempRemoved) == 0:
            return True

        f_solvable = False

def createGameBoard(removedAmount):
    fullBoard = board.buildBoard()
    gameBoard = copy.copy(fullBoard)
    remaining = list(range(0,81))
    removedIndexes = []
    tempRemoved = [0,0]

    for i in range(1000):
        tempRemoved = numberRemove(tempRemoved, remaining, removedIndexes, gameBoard)
        if not solvable(gameBoard,removedIndexes):
            undoRemove(tempRemoved,remaining,removedIndexes,gameBoard)
        if len(removedIndexes) == removedAmount:
            break

    return gameBoard,fullBoard

def solveGameBoard(gameBoard):
    removedIndexes = []
    for i in range(81):
        if gameBoard[i] == 0:
            removedIndexes.append(i)

    print(len(removedIndexes))

    solvable(gameBoard, removedIndexes)


GAMEBOARD = [0,2,0,1,7,8,0,3,0,
             0,4,0,3,0,2,0,9,0,
             1,0,0,0,0,0,0,0,6,
             0,0,8,6,0,3,5,0,0,
             3,0,0,0,0,0,0,0,4,
             0,0,6,7,0,9,2,0,0,
             9,0,0,0,0,0,0,0,2,
             0,8,0,9,0,1,0,6,0,
             0,1,0,4,3,6,0,5,0]

solveGameBoard(GAMEBOARD)











