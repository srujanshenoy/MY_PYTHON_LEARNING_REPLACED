# Variables
Game_Board = [""] * 10


# Functions
def print_board(Board):
    print(
        f"""
    {Board[7]} | {Board[8]} | {Board[9]} 
    {Board[4]} | {Board[5]} | {Board[6]} 
    {Board[1]} | {Board[2]} | {Board[3]}  
    """
    )


def check_win(marker, Board):
    return (
        # Columns
        (
            (Board[1] == Board[4] == Board[7] == marker)
            or (Board[2] == Board[5] == Board[8] == marker)
            or (Board[3] == Board[6] == Board[9] == marker)
        )
        # Rows
        (
            (Board[1] == Board[2] == Board[3] == marker)
            or (Board[4] == Board[5] == Board[6] == marker)
            or (Board[9] == Board[8] == Board[7] == marker)
        )
        # Diagonals
        (
            (Board[1] == Board[5] == Board[9])
            or (Board[3] == Board[5] == Board[7])
        )
    )

def usr_in_request():

    while True:
        print('\n' * 100)
        print_board(Game_Board)
        try:
            usr_in = int(input("Where do you want to play? (0 - 9): "))
        except:
            usr_in_request()

        # Validate input
        if usr_in >= 10:
            pass
        elif usr_in == 0:
            pass
        elif usr_in < 10 and usr_in != 0:
            break

    return usr_in

def place_usr_in(position, board):
    pass

# game loop
usr_in_request()