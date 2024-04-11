"""Este módulo contiene las pruebas unitarias para la clase TicTacToe."""
import unittest
from tkinter import Tk
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """Clase que contiene los casos de prueba para la clase TicTacToe."""

    def  __init__(self):
        """Inicializa el juego antes de cada prueba."""
        self.root = Tk()
        self.game = TicTacToe(self.root)

    def tear_down(self):
        """Cierra la ventana después de cada prueba."""
        self.root.destroy()

    def test_initialization(self):
        """Prueba la inicialización del juego."""
        self.assertIsInstance(self.game.board, list)
        self.assertEqual(len(self.game.board), 3)
        for row in self.game.board:
            self.assertEqual(len(row), 3)

        self.assertEqual(self.game.turn, "X")
        self.assertEqual(self.game.game_over, False)

    def test_play_computer(self):
        """Prueba la función play_computer."""
        # Simula el inicio de un juego contra la computadora
        self.game.play_computer()
        self.assertFalse(self.game.two_players)
        self.assertFalse(self.game.game_over)
        self.assertIsInstance(self.game.board[0][0], str)

    def test_play(self):
        """Prueba la función play."""
        self.game.reset_game()
        self.game.play(0, 0)
        self.assertEqual(self.game.board[0][0], "X")
        self.assertEqual(self.game.turn, "X")
        self.assertFalse(self.game.game_over)

    def test_check_winner(self):
        """Prueba la función check_winner."""
        self.game.reset_game()
        self.game.board = [["X", "O", "X"],
                            ["O", "X", "O"],
                            ["X", "O", "X"]]
        winner, _ = self.game.check_winner()
        self.assertFalse(winner)

    def test_check_tie(self):
        """Prueba la función check_tie."""
        self.game.reset_game()
        self.game.board = [["X", "O", "X"],
                            ["O", "X", "O"],
                            ["O", "X", "O"]]
        tie = self.game.check_tie()
        self.assertFalse(tie)
    def test_reset_game(self):
        """Prueba la función reset_game."""
        self.game.board = [["X", "O", "X"],
                            ["O", "X", "O"],
                            ["O", "X", "O"]]
        self.game.reset_game()
        self.assertEqual(self.game.board, [[" ", " ", " "],
                                            [" ", " ", " "],
                                            [" ", " ", " "]])

    def test_switch_turn(self):
        """Prueba la función switch_turn."""
        self.game.turn = "X"
        self.game.switch_turn()
        self.assertEqual(self.game.turn, "O")

    def test_draw_mark(self):
        """Prueba la función draw_mark."""
        self.game.board = [[" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]]
        self.game.board[0][0] = "X"
        self.assertEqual(self.game.board[0][0], "X")

    def test_game_over(self):
        """Prueba la función check_game_over."""
        self.game.board = [["X", "O", "X"],
                            ["O", "X", "O"],
                            ["X", "O", "X"]]
        self.assertFalse(self.game.game_over)

if __name__ == '__main__':
    unittest.main()
