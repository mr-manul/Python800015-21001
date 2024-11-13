# Connect Four Game

ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'


# Create an empty board
def create_board():
    return [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]


# Print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * (COLUMN_COUNT * 4 - 1))
    print("\n")


# Check if a column is valid for a move
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == EMPTY


# Get the next available row in a column
def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == EMPTY:
            return row


# Place a piece on the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# Check if the last move is a winning move
def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    return False


# Check if the board is full
def is_board_full(board):
    for c in range(COLUMN_COUNT):
        if board[ROW_COUNT - 1][c] == EMPTY:
            return False
    return True


# Main function to play the game
def play_game():
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    while not game_over:
        current_player = PLAYER_1 if turn % 2 == 0 else PLAYER_2
        print(f"Player {current_player}'s turn")

        # Get valid column input from the player
        valid_move = False
        while not valid_move:
            try:
                col = int(input(f"Choose a column (0-{COLUMN_COUNT - 1}): "))
                if 0 <= col < COLUMN_COUNT and is_valid_location(board, col):
                    valid_move = True
                else:
                    print("Invalid move. Column is full or out of bounds.")
            except ValueError:
                print("Please enter a valid integer.")

        # Drop the piece into the board
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, current_player)
        print_board(board)

        # Check if the current player wins
        if winning_move(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        # Check if the board is full and it's a draw
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True

        turn += 1


# Start the game
if __name__ == "__main__":
    play_game()
