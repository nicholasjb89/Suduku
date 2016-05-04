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

    return tempRemoved,remaining,removedIndexes,gameBoard

def undoRemove(tempRemoved, remaining, removedIndexes, gameBoard):
    """undo's the remove"""
    remaining.append(tempRemoved[0])
    gameBoard[tempRemoved[0]] = tempRemoved[1]
    removedIndexes.remove(tempRemoved[0])

    return tempRemoved,remaining,removedIndexes,gameBoard

def solve1(gameBoard, removedIndexes):
    """returns true if it is solvable"""
    gameBoard = copy.copy(gameBoard)
    removedIndexes = copy.copy(removedIndexes)

    f_solvable = False

    while True:
        for index in removedIndexes:
            col = board.getColNumbers(index,gameBoard)
            row = board.getRowNumbers(index,gameBoard)
            square = board.getSquareNumbers(index,gameBoard)

            validNumbers = []
            for n in col:
                if n in row and n in square:
                    validNumbers.append(n)
            if len(validNumbers) == 1:
                gameBoard[index] = validNumbers[0]
                removedIndexes.remove(index)
                f_solvable = True

        if f_solvable == False:
            return gameBoard
        elif len(removedIndexes) == 0:

            return gameBoard

        f_solvable = False

def isSolved(gameBoard):
    for n in gameBoard:
        if n == 0:
            return False
    return True

def createGameBoard(removedAmount):
    fullBoard = board.buildBoard()
    gameBoard = copy.copy(fullBoard)
    remaining = list(range(0,81))
    removedIndexes = []
    tempRemoved = [0,0]

    for i in range(1000):

        tempRemoved,remaining,removedIndexes,gameBoard = numberRemove(tempRemoved, remaining, removedIndexes, gameBoard)
        if not isSolved(solve1(gameBoard, removedIndexes)):
            tempRemoved,remaining,removedIndexes,gameBoard = undoRemove(tempRemoved,remaining,removedIndexes,gameBoard)
        if len(removedIndexes) == removedAmount:
            break
    return gameBoard,fullBoard

def getZeroIndexes(board):
    zeroIndexes = []
    for i in range(len(board)):
        if board[i] == 0:
            zeroIndexes.append(i)
    return zeroIndexes

# def solve2(gameBoard, removedIndexes):
#     gameBoard = copy.copy(gameBoard)
#     removedIndexes = copy.copy(removedIndexes)
#
#     f_solvable = False
#     while True:
#         for index in removedIndexes:
#             squareIndexes = board.getSquareIndexes(index,removedIndexes)
#             totalPossable = [] # [index, [possable numbers]
#                                # [6, [2,3,4,9]],
#                                # [7, [4,9]]
#                                # ]
#             for squareIndex in squareIndexes:
#                 rowNums = board.getRowIndexes(squareIndex,gameBoard)
#                 colNums = board.getColNumbers(squareIndex,gameBoard)
#                 squareNums = board.getSquareNumbers(squareIndex,gameBoard)
#                 indexPossable = [squareIndex,[]] # [6, [2,3,4,9]]
#                 for n in rowNums:
#                     if n in colNums and n in squareNums:
#                         indexPossable[1].append((n))
#                 totalPossable.append(indexPossable)
#
#             numbers = []
#             for iPossable in totalPossable:
#                 for n in iPossable[1]:
#                     numbers.append(n)
#             indexCorrectNumber = 0
#             i = 0
#             while True:
#                 if len(numbers) != 0:
#                     n = numbers.pop(i)
#                     if n not in numbers:
#                         indexCorrectNumber = n
#                         break
#                 else:
#                     break
#             if indexCorrectNumber != 0:
#                 for iPossable in totalPossable:
#                     if indexCorrectNumber in iPossable[1]:
#                         gameBoard[iPossable[0]] = indexCorrectNumber
#                         f_solvable = True
#         if not f_solvable:
#             break
#         f_solvable = False
#
#    return gameBoard

