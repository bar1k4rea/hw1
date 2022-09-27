"""Created by bar1k4real on 27.09.2022."""

import unittest

from main import TicTacGame
from main import NumberNotInRangeError
from main import CellOverflowError


class MyTestCase(unittest.TestCase):
    """Tests"""
    def test_validate_input(self):
        """For check_input"""
        game = TicTacGame()
        self.assertRaises(ValueError, game.check_input, '12asd')
        self.assertRaises(ValueError, game.check_input, 'asd12')
        self.assertRaises(ValueError, game.check_input, 'asd12asd')
        self.assertRaises(NumberNotInRangeError, game.check_input, '0')
        self.assertRaises(NumberNotInRangeError, game.check_input, '10')
        self.assertRaises(NumberNotInRangeError, game.check_input, '100')
        game.board = list(' ' * 9)
        game.board[0] = 'X'
        self.assertRaises(CellOverflowError, game.check_input, 1)
        game.board[4] = 'O'
        self.assertRaises(CellOverflowError, game.check_input, 5)
        game.board[8] = 'X'
        self.assertRaises(CellOverflowError, game.check_input, 9)

    def test_check_winner(self):
        """For check_winner"""
        game = TicTacGame()
        game.board = list(' ' * 9)
        game.board[0] = 'X'
        game.board[1] = 'X'
        game.board[2] = 'X'
        self.assertEqual(True, game.check_winner())
        game.board = list(' ' * 9)
        self.assertEqual(False, game.check_winner())
        game.board = list(' ' * 9)
        game.board[2] = 'O'
        game.board[5] = 'O'
        game.board[8] = 'O'
        self.assertEqual(True, game.check_winner())


if __name__ == '__main__':
    unittest.main()
