from board import Board, textToBoard

class AutoAdjuster(object):
    def __init__(self,boardClass):
        self.Board = boardClass()

        self.valuableIndexes = 5
        self.newSeed = 5
        self.previus = []

    def solve(self,boards):
        solved = 0
        failed = 0

        for i in range(0,20):
            board = boards[i]
            b = self.Board.solver.solve(board,self.valuableIndexes, self.newSeed)
            if self.Board.validate.validate(b):
                solved += 1
            else :
                failed += 1
        self.previus.append((solved,(self.newSeed,self.valuableIndexes)))

    def adjust(self):
        boards = textToBoard("C:\\Users\\Bailey\\Documents\\GitHub\\Suduku\\Hard.txt")
        while self.valuableIndexes != 20:
            self.solve(boards)
            self.newSeed += 5
            if self.newSeed == 100:
                self.newSeed = 5
                self.valuableIndexes+=1
            print(self.valuableIndexes,self.newSeed)

        return self.previus.sort()


a = AutoAdjuster(Board)
all = a.adjust()

for i in all:
    print(i)








