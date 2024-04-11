# TicTacToe

Este proyecto implementa el clásico juego Tic Tac Toe (Tres en Raya) en Python utilizando la biblioteca tkinter para la interfaz gráfica. El juego permite jugar contra la computadora o contra otro jugador humano.

## Características

- La clase `TicTacToe` maneja la lógica del juego y la interfaz gráfica.
- Se utiliza una matriz `board` para representar el estado del tablero.
- Los botones de la interfaz gráfica se crean dinámicamente para representar cada celda del tablero.
- La función `play` se encarga de realizar un movimiento en el juego, actualizando el tablero y verificando si hay un ganador o empate.
- La función `check_winner` verifica si hay un ganador en el juego.
- La función `check_tie` verifica si hay un empate en el juego.
- La función `end_game` finaliza el juego y muestra el mensaje de resultado.

## Uso

Para ejecutar el juego, simplemente ejecuta el archivo `main.py`:

```bash
python main.py
```

## Requisitos

- Python 3.10 o superior
- Biblioteca tkinter (incluida en la instalación estándar de Python)

## Créditos
Este proyecto fue desarrollado por Daniel Escobar.
