WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
    (0, 4, 8), (2, 4, 6) # Diagonals
]

def print_board(board):
    print("-------------")
    for i in range(0, 9, 3):
        print("| " + " | ".join(board[i:i+3]) + " |")
        print("-------------")

def check_win(board):
    for combo in WINNING_COMBINATIONS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def tic_tac_toe():
    board = [" "]*9
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn.")
        move = int(input("Enter a position (1-9): "))
        if 1 <= move <= 9 and board[move-1] == " ":
            board[move-1] = player
            if check_win(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if " " not in board:
                print_board(board)
                print("Tie game!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("Invalid move, please try again.")

tic_tac_toe()
