from board import *
import unittest

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

class build_board(unittest.TestCase):
    def test_build(self):
        board = Board(Solve)
        full = False
        if 0 not in board.getBoard():
            full = True

        self.assertEqual(full, True)

class solve_board_easy(unittest.TestCase):
    def test_solve(self):
        solved = Solve().solve(EASYGAMEBOARD)
        self.assertEqual(solved,EASYSOLVEDGAMEBOARD)


if __name__ == "__main__":
    unittest.main()

