import random

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


def getRowNumbers(index, board):
    validNumbers = list(range(1,10))

    offset = index%9
    index -= offset

    for i in range(index,index+9):
        if board[i] != 0:
            validNumbers.remove(board[i])

    return validNumbers

def getColNumbers(index, board):
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

def getSquareNumbers(index, board):
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

def attemptBoard():
    board = [0] * 81
    for i in range(81):
        rowNums = getRowNumbers(i,board)
        colNums = getColNumbers(i,board)
        squareNums = getSquareNumbers(i, board)

        validNumbers = []

        for n in rowNums:
            if n in colNums and n in squareNums:
                validNumbers.append(n)
        try:
            board[i] = random.choice(validNumbers)
        except:
            break
    return board

def buildBoard():
    i = 0
    while True:
        i += 1
        board = attemptBoard()
        if 0 not in board:
            row = []
            index = 0
            for num in board:
                row.append(num)
                if index == 8:

                    row = []
                    index = -1

                index += 1
            break
    return board


if __name__ == "main":
    buildBoard()




