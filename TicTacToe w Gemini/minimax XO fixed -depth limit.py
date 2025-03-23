import tkinter as tk
from tkinter import messagebox
from functools import lru_cache

class TicTacToe:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_board()

    def get_board_state(self):
        return tuple(tuple(self.buttons[i][j]["text"] for j in range(3)) for i in range(3))

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Arial", 40), width=3, height=1,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def handle_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.current_player == "X":
            self.make_move(row, col)

    def make_move(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.check_for_winner()
            self.switch_player()

            if self.current_player == "O":  # AI's turn
                self.ai_move()

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

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.start()  # Restart the game loop
    
    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        current_board = self.get_board_state()

        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    new_board = list(list(row) for row in current_board)
                    new_board[i][j] = "O"
                    new_board_tuple = tuple(tuple(row) for row in new_board)
                    score = self.minimax(new_board_tuple, 0, False)

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            self.make_move(best_move[0], best_move[1])


    @lru_cache(maxsize=None)
    def minimax(self, board_state, depth, is_maximizing):
        # Check for terminal states using the board_state
        if self.check_winner_for_minimax_cached(board_state, "O"):
            return 10 - depth
        if self.check_winner_for_minimax_cached(board_state, "X"):
            return -10 + depth
        if self.is_board_full_cached(board_state):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board_state[i][j] == "":
                        # Create new board state
                        new_board = list(list(row) for row in board_state)
                        new_board[i][j] = "O"
                        new_board_tuple = tuple(tuple(row) for row in new_board)
                        score = self.minimax(new_board_tuple, depth + 1, False)
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board_state[i][j] == "":
                        # Create new board state
                        new_board = list(list(row) for row in board_state)
                        new_board[i][j] = "X"
                        new_board_tuple = tuple(tuple(row) for row in new_board)
                        score = self.minimax(new_board_tuple, depth + 1, True)
                        best_score = min(score, best_score)
            return best_score

    def check_winner_for_minimax_cached(self, board_state, player):
        # Check rows
        for i in range(3):
            if all(board_state[i][j] == player for j in range(3)):
                return True
    
        # Check columns
        for j in range(3):
            if all(board_state[i][j] == player for i in range(3)):
                return True
    
        # Check diagonals
        if all(board_state[i][i] == player for i in range(3)):
            return True
        if all(board_state[i][2 - i] == player for i in range(3)):
            return True
    
        return False
    
    def is_board_full_cached(self, board_state):
        return all(board_state[i][j] != "" for i in range(3) for j in range(3))
    

    # @lru_cache
    def check_winner_for_minimax(self, player):
        # Check rows
        for i in range(3):
            if all(self.buttons[i][j]["text"] == player for j in range(3)):
                return True

        # Check columns
        for j in range(3):
            if all(self.buttons[i][j]["text"] == player for i in range(3)):
                return True

        # Check diagonals
        if all(self.buttons[i][i]["text"] == player for i in range(3)):
            return True
        if all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False
        return True

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()