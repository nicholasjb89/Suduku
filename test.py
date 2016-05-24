from board import *
import unittest
import time

NOTVALIDBOARD = [7, 4, 5, 9, 6, 3, 8, 2, 1,
                 3, 5, 7, 4, 1, 2, 6, 8, 9,
                 8, 7, 2, 6, 4, 1, 9, 3, 5,
                 4, 6, 1, 5, 9, 8, 2, 7, 3,
                 9, 2, 6, 3, 8, 5, 4, 1, 7,
                 5, 1, 3, 8, 2, 9, 7, 6, 4,
                 2, 3, 4, 7, 5, 6, 1, 9, 8,
                 1, 9, 8, 2, 3, 7, 5, 4, 6,
                 6, 8, 9, 1, 7, 4, 3, 5, 2]

VALIDBOARD = [9,3,6,8,1,7,4,5,2,
            4,8,5,2,3,6,7,9,1,
            7,2,1,4,9,5,6,8,3,
            8,4,3,5,6,9,2,1,7,
            2,1,7,3,4,8,9,6,5,
            5,6,9,7,2,1,3,4,8,
            3,5,8,6,7,4,1,2,9,
            6,9,2,1,8,3,5,7,4,
            1,7,4,9,5,2,8,3,6]

EASYGAMEBOARD = [1,0,5,0,0,0,2,0,3,
                 0,3,8,7,5,6,4,1,0,
                 0,0,0,0,0,0,0,0,0,
                 0,2,0,9,0,8,0,3,0,
                 0,0,9,0,0,0,1,0,0,
                 0,4,0,6,0,2,0,7,0,
                 0,0,0,0,0,0,0,0,0,
                 0,1,3,4,9,5,7,8,0,
                 7,0,4,0,0,0,3,0,6]

EASYSOLVEDGAMEBOARD = [1,7,5,8,4,9,2,6,3,
                       2,3,8,7,5,6,4,1,9,
                       4,9,6,1,2,3,8,5,7,
                       5,2,7,9,1,8,6,3,4,
                       3,6,9,5,7,4,1,2,8,
                       8,4,1,6,3,2,9,7,5,
                       9,8,2,3,6,7,5,4,1,
                       6,1,3,4,9,5,7,8,2,
                       7,5,4,2,8,1,3,9,6]

MEDIUMGAMEBOARD = [6,0,0,8,0,0,0,0,0,
                   0,0,1,9,2,7,0,0,8,
                   0,9,0,3,0,0,0,7,1,
                   9,2,0,0,7,0,0,3,6,
                   0,0,6,0,0,8,0,0,0,
                   0,0,0,0,9,0,0,2,5,
                   1,0,0,0,0,0,0,0,2,
                   2,6,8,5,4,0,0,0,0,
                   0,0,5,7,1,0,6,0,9]

MEDIUMSOLVEDGAMEBOARD = [6,3,7,8,5,1,2,9,4,
                         4,5,1,9,2,7,3,6,8,
                         8,9,2,3,6,4,5,7,1,
                         9,2,4,1,7,5,8,3,6,
                         5,1,6,2,3,8,9,4,7,
                         7,8,3,4,9,6,1,2,5,
                         1,7,9,6,8,3,4,5,2,
                         2,6,8,5,4,9,7,1,3,
                         3,4,5,7,1,2,6,8,9]

WORLDHARDEST = [8,0,0,0,0,0,0,0,0,
                0,0,3,6,0,0,0,0,0,
                0,7,0,0,9,0,2,0,0,
                0,5,0,0,0,7,0,0,0,
                0,0,0,0,4,5,7,0,0,
                0,0,0,1,0,0,0,3,0,
                0,0,1,0,0,0,0,6,8,
                0,0,8,5,0,0,0,1,0,
                0,9,0,0,0,0,4,0,0]

SOLVEDWORLHARDEST = [8,1,2,7,5,3,6,4,9,
                     9,4,3,6,8,2,1,7,5,
                     6,7,5,4,9,1,2,8,3,
                     1,5,4,2,3,7,8,9,6,
                     3,6,9,8,4,5,7,2,1,
                     2,8,7,1,6,9,5,3,4,
                     5,2,1,9,7,4,3,6,8,
                     4,3,8,5,2,6,9,1,7,
                     7,9,6,3,1,8,4,5,2]

WORLDHARDESTWITH10MORE = [8,0,0,0,0,0,0,0,0,
                          0,4,3,6,0,0,0,0,0,
                          0,7,5,4,9,0,2,8,0,
                          0,5,0,0,0,7,0,0,0,
                          0,0,0,0,4,5,7,0,0,
                          0,0,0,1,0,0,0,3,4,
                          0,0,1,0,7,0,3,6,8,
                          0,0,8,5,0,0,9,1,0,
                          0,9,0,0,0,0,4,5,0]

class Build_board(unittest.TestCase):
    def test_if_valid_board(self):
        board = Board()
        board.build()
        fullBoard = board.getSolvedBoard()
        valid = board.validate.validate(fullBoard)
        self.assertEqual(valid, True)

    def test_failed_board_percent(self):
        failed = 0
        for i in range(0,25):
            board = Board()
            board.build()
            failed += board.failed
        print("Average Board().build() fail rate =", failed/25)
        self.assertLess(failed/25,500)

    def test_makeBoard(self):
        board = Board()
        board.build()
        sudoku = board.getBoard()
        solved = board.solver.solve(sudoku)

        self.assertEqual(solved,board.getSolvedBoard())

class Solve_board_easy(unittest.TestCase):
    def test_solve(self):
        board = Board()
        solved = board.solver.solve(EASYGAMEBOARD)
        self.assertEqual(solved,EASYSOLVEDGAMEBOARD)

class Solve_board_medium(unittest.TestCase):
    def test_solve(self):
        board = Board()
        solved = board.solver.solve(MEDIUMGAMEBOARD)
        self.assertEqual(solved,MEDIUMSOLVEDGAMEBOARD)

class solve_board_worldHardest(unittest.TestCase):
    def test_solve(self):
        solved = Board(Solve,Validate).solver.solve(WORLDHARDEST)
        time.sleep(.2)

        compare(solved,SOLVEDWORLHARDEST)
        self.assertEqual(solved,SOLVEDWORLHARDEST,displayBoard(solved,"Worlds Hardest Board"))


class Validate_board(unittest.TestCase):
    def test_validate_pass(self):
        board = Board()
        valid = board.validate.validate(EASYSOLVEDGAMEBOARD)

        self.assertEqual(valid,True)

    def test_validate_fail(self):
        board = Board()
        valid = board.validate.validate(NOTVALIDBOARD)

        self.assertEqual(valid,False)

if __name__ == "__main__":
    unittest.main()


