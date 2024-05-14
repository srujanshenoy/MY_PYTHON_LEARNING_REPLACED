# make tic tac toe game tht has a GUI
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.buttons = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Arial", 40), width=3, height=1,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.check_for_winner()
            self.switch_player()

    def check_for_winner(self):
        # Check rows
        for i in range(3):
            if all(self.buttons[i][j]["text"] == self.current_player for j in range(3)):
                self.announce_winner()
                return

        # Check columns
        for j in range(3):
            if all(self.buttons[i][j]["text"] == self.current_player for i in range(3)):
                self.announce_winner()
                return

        # Check diagonals
        if all(self.buttons[i][i]["text"] == self.current_player for i in range(3)):
            self.announce_winner()
            return
        if all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            self.announce_winner()
            return

        # Check for tie
        if all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            self.announce_tie()

    def announce_winner(self):
        messagebox.showinfo("Winner", f"{self.current_player} wins!")
        self.ask_for_restart()

    def announce_tie(self):
        messagebox.showinfo("Tie", "It's a tie!")
        self.ask_for_restart()

    def ask_for_restart(self):
        restart = messagebox.askquestion("Play Again?", "Do you want to play again?")
        if restart == "yes":
            self.reset_game()
            self.start()  # Restart the game loop

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                # Call config method to change text
                self.buttons[i][j].config(text="")
        self.current_player = "X"

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()
