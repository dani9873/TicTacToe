import tkinter as tk
from tkinter import Button, Label, OptionMenu, messagebox
from random import randint 

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.master.configure(bg='dark gray')
        
        # Colores utilizados en los botones y para resaltar el ganador
        self.button_bg = "#475053"
        self.button_fg = "#BFC7CA"
        self.winner_color = "#EEB43F"
     
        # Inicializa el juego
        self.initialize_game()

    def initialize_game(self):
        # Inicializa el tablero y crea los botones        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[self.create_button(i, j) for j in range(3)] for i in range(3)]
        self.display_buttons()

        # Muestra el turno actual y estado del juego
        self.turn = "X"
        self.message = self.create_message()
        self.message.grid(row=3, column=0, columnspan=3, pady=10)

        self.game_over = True
        self.two_players = False
        
        # Crea el menú de inicio y el botón de reinicio
        self.create_start_menu().grid(row=4, column=0, columnspan=3, pady=10)
        self.create_reset_button().grid(row=5, column=0, columnspan=3, pady=10)

    def create_button(self, x, y):
        # Crea un botón con el texto vacío y la función de juego correspondiente a la posición
        return Button(
            self.master, text=" ", font=("Courier New", 24, "bold"), bg=self.button_bg, fg=self.button_fg, width=4, height=1,
            command=lambda: self.play(x, y)
            )

    def display_buttons(self):
        # Muestra los botones en la ventana
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def create_message(self):
        # Crea una etiqueta para mostrar el turno actual
        return Label(self.master, text="Turn: X", font=("Courier New", 20), bg='dark gray', fg='white')

    def create_start_menu(self):
        # Crea un menú desplegable para seleccionar el modo de juego
        start_menu = tk.StringVar(self.master)
        start_menu.set("Select a game mode")
        return OptionMenu(
            self.master, start_menu, "Playing against the computer", 
            "Play against another player", command=self.select_mode
            )
        
    def create_reset_button(self):
        # Crea un botón de reinicio
        return Button(
            self.master, text="Reset", font=("Courier New", 15), 
            command=self.reset_game
            )
    
    def select_mode(self, mode):
        # Función para seleccionar el modo de juego
        if mode == "Playing against the computer":
            self.play_computer()
        elif mode == "Play against another player":
            self.two_players = True
            self.reset_game()

    def play_computer(self):
        # Inicia un juego contra la computadora
        self.two_players = False
        self.reset_game()
        
    def reset_game(self):
        # Reinicia el juego
        self.board = [[" " for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        self.turn = "X"
        self.message.config(text="Turn: X")
        self.game_over = False

    def play(self, x, y):
        # Función principal para jugar
        if self.board[x][y] == " " and not self.game_over:
            self.board[x][y] = self.turn
            self.buttons[x][y].config(text=self.turn)
            self.buttons[x][y].config(fg="#939A9F")
            winner, winning_line = self.check_winner()
            if winner:
                self.end_game(self.turn, winning_line)
            elif self.check_tie():
                self.message.config(text="Tie game!")
                self.game_over = True
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.message.config(text=f"Turn: {self.turn}")
                if self.turn == "O" and not self.two_players:
                    self.computer_play()

    def computer_play(self):
        # Movimiento de la computadora
        x, y = self.get_best_move()
        self.play(x, y)

    def get_best_move(self):
        # Lógica para determinar el mejor movimiento para la computadora
        def check_move(player, positions):
            (x1, y1), (x2, y2), (x3, y3) = positions
            if self.buttons[x1][y1]['text'] == self.buttons[x2][y2]['text'] == player and self.buttons[x3][y3]['text'] == ' ':
                return (x3, y3)
            if self.buttons[x1][y1]['text'] == self.buttons[x3][y3]['text'] == player and self.buttons[x2][y2]['text'] == ' ':
                return (x2, y2)
            if self.buttons[x2][y2]['text'] == self.buttons[x3][y3]['text'] == player and self.buttons[x1][y1]['text'] == ' ':
                return (x1, y1)
            return None

        # Combinaciones de posiciones para las líneas
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        # Verificar movimientos ganadores o bloqueos para 'O' y 'X'
        for player in ('O', 'X'):
            for line in lines:
                move = check_move(player, line)
                if move:
                    return move
            # Si no hay movimientos ganadores, intentar bloquear al oponente
        opponent = 'X' if self.turn == 'O' else 'O'
        for line in lines:
            move = check_move(opponent, line)
            if move:
                return move
        # Tomar el centro si está libre
        if self.buttons[1][1]['text'] == ' ':
            return 1, 1
        # Elegir una esquina si está libre
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        empty_corners = [corner for corner in corners if self.buttons[corner[0]][corner[1]]['text'] == ' ']
        if empty_corners:
            return empty_corners[randint(0, len(empty_corners) - 1)]
        
        # Elegir una posición aleatoria si no hay movimientos ganadores o bloqueos
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ' ']
        return empty_cells[randint(0, len(empty_cells) - 1)] if empty_cells else (randint(0, 2), randint(0, 2))
    
    def check_winner(self):
        # Verifica si hay un ganador
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for line in lines:
            if self.buttons[line[0][0]][line[0][1]]['text'] == self.buttons[line[1][0]][line[1][1]]['text'] == self.buttons[line[2][0]][line[2][1]]['text'] != ' ':
                return True, line

        return False, []

    def check_tie(self):
        # Verifica si hay un empate
        return all(self.buttons[i][j]['text'] != ' ' for i in range(3) for j in range(3))

    def end_game(self, winner,winning_line):
        # Finaliza el juego y muestra el mensaje de resultado
        self.game_over = True
        if winner == 'tie':
            message = "Tie game!"
        else:
            message = f"{winner} wins!"
        
        for coord in winning_line:
           self.buttons[coord[0]][coord[1]].config(fg=self.winner_color)
        
        self.message.config(text=message)
        
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
            
        if play_again:
            self.reset_game()
        else:
            self.initialize_game()
