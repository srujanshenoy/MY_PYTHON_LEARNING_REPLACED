# Variables
Game_Board = [""] * 9


# Functions
def print_board(Game_Board):
    print(
        f"""
    {Game_Board[7]} | {Game_Board[8]} | {Game_Board[9]} 
    {Game_Board[4]} | {Game_Board[5]} | {Game_Board[6]} 
    {Game_Board[1]} | {Game_Board[2]} | {Game_Board[3]}  
    """
    )


def check_win(marker, Game_Board):
    return (
        # Columns
        (
            (Game_Board[1] == Game_Board[4] == Game_Board[7] == marker)
            or (Game_Board[2] == Game_Board[5] == Game_Board[8] == marker)
            or (Game_Board[3] == Game_Board[6] == Game_Board[9] == marker)
        )
        # Rows
        (
            (Game_Board[1] == Game_Board[2] == Game_Board[3] == marker)
            or (Game_Board[4] == Game_Board[5] == Game_Board[6] == marker)
            or (Game_Board[9] == Game_Board[8] == Game_Board[7] == marker)
        )
        # Diagonals
        (
            (Game_Board[1] == Game_Board[5] == Game_Board[9])
            or (Game_Board[3] == Game_Board[5] == Game_Board[7])
        )
    )


# game loop
