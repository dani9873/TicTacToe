import unittest
from tkinter import Tk
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.game = TicTacToe(self.root)
    
    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.assertIsInstance(self.game.board, list)
        self.assertEqual(len(self.game.board), 3)
        for row in self.game.board:
            self.assertEqual(len(row), 3)

        self.assertEqual(self.game.turn, "X")
        self.assertEqual(self.game.game_over, True)
        
    def test_play_computer(self):
        # Simula el inicio de un juego contra la computadora
        self.game.play_computer()
        self.assertFalse(self.game.two_players)
        self.assertFalse(self.game.game_over)
        # Agrega más aserciones según sea necesario

    def test_play(self):
        self.game.reset_game()
        self.game.play(0, 0)
        self.assertEqual(self.game.board[0][0], "X")
        self.assertEqual(self.game.turn, "X")
        self.assertFalse(self.game.game_over)

    def test_check_winner(self):
        self.game.reset_game()
        self.game.board = [["X", "O", "X"],
                            ["O", "X", "O"],
                            ["X", "O", "X"]]
        winner, _ = self.game.check_winner()
        self.assertFalse(winner)

    def test_check_tie(self):
        self.game.reset_game()
        self.game.board = [["X", "O", "X"],
                            ["O", "X", "O"],
                            ["O", "X", "O"]]
        tie = self.game.check_tie()
        self.assertFalse(tie)

if __name__ == '__main__':
    unittest.main()
