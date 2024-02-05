from tkinter import *
from tkinter import messagebox
import random

# Create the game board
board = [' ' for _ in range(9)]

# Check if a player has won
def check_win(player):
    # Row win
    if (board[0] == board[1] == board[2] == player) or \
       (board[3] == board[4] == board[5] == player) or \
       (board[6] == board[7] == board[8] == player):
        return True
    # Column win
    if (board[0] == board[3] == board[6] == player) or \
       (board[1] == board[4] == board[7] == player) or \
       (board[2] == board[5] == board[8] == player):
        return True
    # Diagonal win
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

# Check if the game has ended in a draw
def check_draw():
    return ' ' not in board

# AI player's turn
def ai_turn():
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'
    buttons[move]['text'] = 'O'
    if check_win('O'):
        messagebox.showinfo('Game Over', 'You lost!')
        reset_game()
    elif check_draw():
        messagebox.showinfo('Game Over', 'It\'s a draw!')
        reset_game()

# Handle player's turn
def player_turn(i):
    if board[i] == ' ':
        buttons[i]['text'] = 'X'
        board[i] = 'X'
        if check_win('X'):
            messagebox.showinfo('Game Over', 'Congratulations, you won!')
            reset_game()
        elif check_draw():
            messagebox.showinfo('Game Over', 'It\'s a draw!')
            reset_game()
        else:
            ai_turn()

# Reset the game
def reset_game():
    for i in range(9):
        board[i] = ' '
        buttons[i]['text'] = ' '
    messagebox.showinfo('New Game', 'Let\'s play again!')

# Create the GUI
root = Tk()
root.title('Tic Tac Toe')

buttons = []
for i in range(9):
    button = Button(root, text=' ', command=lambda i=i: player_turn(i))
    button.grid(row=i//3, column=i%3, sticky='news')
    buttons.append(button)

reset_button = Button(root, text='Reset', command=reset_game)
reset_button.grid(row=3, column=1, columnspan=2, sticky='news')

# Start the game
ai_turn()

# Run the GUI main loop
root.mainloop()