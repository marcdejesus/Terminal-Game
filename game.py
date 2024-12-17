# Method to print game in ascii (board will be a 3x3 2d array)
def print_game(board):
    pass

# Method for AI to make a decision on what move to play
def ai_play(board):
    return board

# Method for player to make a decision to play
def play(board):
    move = input("Please input the coordinates of your next move: ") # Looking for a num num approach
    board[move.split(" ")[0]][move.split(" ")[1]] = "X"
    return board

# Method to check if game is over
def check_game_status(board):
    pass

# While loop that will hold the game inside of it