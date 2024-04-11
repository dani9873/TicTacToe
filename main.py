import tkinter as tk
from tictactoe import TicTacToe

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
