import os

# Method to print game in ascii (board will be a 3x3 2d array)
def print_game(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Method for AI to make a decision on what move to play. For now, fills first available spot.
def ai_play(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                return board
    return board

# Method for player to make a decision to play
def play(board):
    move = input("Please input the coordinates of your next move (row col): ") # Looking for a num num approach
    row, col = map(int, move.split())
    try:
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("This coordinate is taken, try again.")
            return play(board)
    except:
        print("Coordinates must be in range 0-2, try again.")
        return play(board)
    return board

# Method to check if game is over
def check_game_status(board):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    # Check for a draw
    for row in board:
        if " " in row:
            return False
    return True

# Initialize the board
board = [[" " for i in range(3)] for i in range(3)]

# While loop that will hold the game inside of it.
# The game will be over when the check_game_status returns True
while not check_game_status(board):
    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal
    board = play(board)
    board = ai_play(board)
    print_game(board)

print("Game Over!")