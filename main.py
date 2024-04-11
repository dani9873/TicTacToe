"""
Módulo principal para ejecutar el juego Tic Tac Toe con interfaz gráfica.

Utiliza la biblioteca tkinter para la interfaz gráfica y la clase TicTacToe del módulo tictactoe.

"""
import tkinter as tk
from tictactoe import TicTacToe

# Inicializa la aplicación tkinter y el juego Tic Tac Toe
if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
