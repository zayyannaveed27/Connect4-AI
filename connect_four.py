from copy import deepcopy
import random

COLUMNS = 7
ROWS = 6

HUMAN = 0
AI = 1

PLAYER1 = 0
PLAYER2 = 1

def create_board():
    """
    Create and return a new Connect 4 board.

    Returns:
        list of list: A 6x7 grid initialized with empty spaces represented as " ".
    """
    return [[" "] * COLUMNS for _ in range(ROWS)]

def print_board(board):
    """
    Print the Connect 4 board.

    Args:
        board (list of list): The current state of the Connect 4 board.
    """
    print("\n  " + " ".join(f" {i+1} " for i in range(COLUMNS)))
    print("+" + "---+" * COLUMNS)
    for row in board:
        print("|" + "|".join(("🔴 " if cell == PLAYER1 else "🔵 " if cell == PLAYER2 else "   ") for cell in row) + "|")
        print("+" + "---+" * COLUMNS)

def generate_random_move(board):
    """
    Generate a random valid move for Connect 4.

    Args:
        board (list of list): The current board state.

    Returns:
        int: A random column number where a valid move can be made.
    """
    possible_moves = find_possible_moves(board)
    return random.choice(possible_moves)




def make_move(board, col, piece):
    """
    Make a move on the board.

    Args:
        board (list of list): The current board state.
        col (int): The column number where the piece is to be placed.
        piece (int): The player piece (PLAYER1 or PLAYER2).

    Returns:
        bool: True if the move was successful, False otherwise.
    """
    for row in reversed(board):
        if row[col-1] == ' ':
            row[col-1] = piece
            return True
    return False

def is_valid_move(board, col):
    """
    Check if a move is valid.

    Args:
        board (list of list): The current board state.
        col (int): The column number to check.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    if col < 1 or col > COLUMNS:
        return False
    return board[0][col-1] == ' '

def find_possible_moves(board):
    """
    Find all possible moves for the current board state.

    Args:
        board (list of list): The current board state.

    Returns:
        list: A list of column numbers where a move can be made.
    """
    return [col+1 for col in range(COLUMNS) if is_valid_move(board, col+1)]

def has_won(board, piece):
    """
    Check if a player has won the game.

    Args:
        board (list of list): The current board state.
        piece (int): The player piece to check for a win (PLAYER1 or PLAYER2).

    Returns:
        bool: True if the specified player has won, False otherwise.
    """
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == piece:
                return True

    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == piece:
                return True

    # Check diagonal (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == piece:
                return True

    # Check diagonal (negative slope)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == piece:
                return True

    return False



def game_finished(board):
    """
    Check if the game is finished.

    Args:
        board (list of list): The current board state.

    Returns:
        bool: True if the game is finished, False otherwise.
    """
    return has_won(board, PLAYER1) or has_won(board, PLAYER2) or find_possible_moves(board) == []

def random_eval(board):
    """
    Evaluate the board state randomly.

    Args:
        board (list of list): The current board state.

    Returns:
        int: A random score for the board state.
    """
    return random.randint(-100,100)




def get_human_player_move(board):
    """
    Prompt human player to input their move.

    Args:
        board (list of list): The current board state.

    Returns:
        int: The column number chosen by the human player.
    """
    
    selected_move = int(input("Please select a column to place your piece (enter -1 to terminate):\n"))

    while selected_move != -1 and not is_valid_move(board, selected_move):
        print("Invalid move. Please try again.")
        selected_move = int(input("Please select a column to place your piece (enter -1 to terminate):\n"))

    return selected_move
        
        
def play_random_game(is_human=True):
    """
    Play a game of Connect 4 with random computer

    Args:
        is_human (bool): True if Player 1 is human, False if Player 1 is an AI player.
    """
    board = create_board()
    print_board(board)
    print()

    current_player = PLAYER1

    while not game_finished(board):
        if current_player == PLAYER1:
            if is_human:
                move = get_human_player_move(board)
                if move == -1:
                    print("Game terminated")
                    return
            else:
                print("AI 1's turn")
                move = generate_random_move(board)
        else:
            print("AI 2's turn")
            move = generate_random_move(board)

        print(f"Selected: {move}")
        make_move(board, move, current_player)
        print_board(board)
        print()

        if has_won(board, current_player):
            print(f"Player {current_player + 1} won!")
            break

        # Switch players
        current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

    if not has_won(board, PLAYER1) and not has_won(board, PLAYER2):
        print("Game is tied!")

        
def play_game(player1 = HUMAN,depth1 = 4, eval_func1 = random_eval,depth2 = 4, eval_func2 = random_eval):
    """
    Play a game of Connect 4.

    Args:
        player1 (int): The type of the first player (HUMAN or AI).
        depth1 (int): The depth of recursion for player1 if AI.
        depth2 (int): The depth of recursion for player2.
        eval_func1 (function): The heuristic function for player1 if AI.
        eval_func2 (function): The heuristic function for player2.
    """
    board = create_board()
    print_board(board)
    print()
    while not game_finished(board):
      if player1 == HUMAN:
          move = get_human_player_move(board)
      else:
        print( "AI 1 turn")
        move, score = minimax(board, True, depth1, -float("Inf"), float("Inf"), eval_func1)
      print( "Selected: ", move)
      make_move(board, move, PLAYER1)
      print_board(board)
      print()

      if not game_finished(board):

        result = minimax(board, False, depth2, -float("Inf"), float("Inf"), eval_func2)
        print("AI 2 turn")
        print( "Selected:", result[0])
        make_move(board, result[0], PLAYER2)
        print_board(board)
        print()
    if has_won(board, PLAYER1):
        print("Player 1 won!")
    elif has_won(board, PLAYER2):
        print("Player 2 won!")
    else:
        print("Game is tied!")
