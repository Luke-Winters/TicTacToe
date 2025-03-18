def print_board(board: list[[str]]) -> str:
    """Prints the 3x3 game board as a single str"""
    
    return f"""
  
 {board[0][0]} | {board[0][1]} | {board[0][2]} 
-----------
 {board[1][0]} | {board[1][1]} | {board[1][2]}    
-----------
 {board[2][0]} | {board[2][1]} | {board[2][2]}

"""

def is_winner(board: list[[str]]) -> bool:
    """Determines if a player has won the game"""
    
    if board[0][0] == board[0][1] == board[0][2] and board[0][2] != " ":
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][2] != " ":
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][2] != " ":
        return True
    elif board[0][0] == board[1][0] == board[2][0] and board[2][0] != " ":
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[2][2] != " ":
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[2][2] != " ":
        return True
    elif board[2][0] == board[1][1] == board[0][2] and board[0][2] != " ":
        return True
    else:
        return False
    
def mark_square(board: list[[str]], mark: str, cell: str) -> list[[str]]:
    """Marks a square with the given player's symbol on the game board"""
    
    row = int(cell[0])
    column = int(cell[2])
    board[row][column] = mark
    return board

def get_choice() -> str:
    """Gets the choice of where the player would like to place their mark"""
    
    return input("Where would you like to play (row,column) ")

def play_game():
    """Plays the game of tic-tac-toe"""
    game_board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "] ]
    print(print_board(game_board))
    turn = 1
    mark = ""
    while True:
        choice = get_choice()
        num_choice = choice.strip(",")
        row = int(num_choice[0])
        column = int(num_choice[2])
        if turn % 2 == 0:
            mark = "O"
        else:
            mark = "X"
        if game_board[row][column] != " ":
            print(f"\nThere is already an {game_board[row][column]} there.")
            print(print_board(game_board))
        else:
            game_board = mark_square(game_board, mark, choice)
            print(print_board(game_board))
            if is_winner(game_board):
                print(f"{mark}'s Win!!")
                break
            turn += 1

game = True
while game:
    play_game()
    answer = input("\nWould you like to play again? (y/n)")
    if answer != "y":
        print("Game Finished")
        game = False

