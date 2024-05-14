import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.canvas = Canvas(self.window, width=300, height=350)
        self.canvas.pack()

        self.buttons = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.player1_score = 0
        self.player2_score = 0
        self.create_board()
        self.create_scoreboard()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                x1 = j * 100
                y1 = i * 100
                x2 = x1 + 100
                y2 = y1 + 100

                self.canvas.create_rectangle(x1, y1, x2, y2, width=2, outline="black", tags=f"button_{i}_{j}")
                self.round_rectangle(x1, y1, x2, y2, radius=10, tags=f"button_{i}_{j}")

                button = tk.Button(self.canvas, text="", font=("Arial", 40), width=3, height=1,
                                   command=lambda row=i, col=j: self.handle_click(row, col),
                                   relief="flat", bd=0)
                self.canvas.create_window((x1 + x2) / 2, (y1 + y2) / 2, window=button)
                self.buttons[i][j] = button

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1]
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def create_scoreboard(self):
        self.score_label = tk.Label(self.canvas, text=f"Player 1: {self.player1_score} - Player 2: {self.player2_score}",
                                   font=("Arial", 16))
        self.canvas.create_window(150, 325, window=self.score_label)

    def handle_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.make_move(row, col)

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
        if self.current_player == "X":
            self.player1_score += 1
        else:
            self.player2_score += 1
        self.update_scoreboard()
        self.ask_for_restart()

    def announce_tie(self):
        messagebox.showinfo("Tie", "It's a tie!")
        self.ask_for_restart()

    def ask_for_restart(self):
        restart = messagebox.askquestion("Play Again?", "Do you want to play again?")
        if restart == "yes":
            self.reset_game()
        else:
            self.window.destroy()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.start()

    def update_scoreboard(self):
        self.score_label.config(text=f"Player 1: {self.player1_score} - Player 2: {self.player2_score}")

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()