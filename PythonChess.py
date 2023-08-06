import chess
import chess.engine

# Function to display the chess board as Unicode characters
def display_board(board):
    return board.unicode()

# Function to get the player's move
def get_player_move(board):
    while True:
        try:
            move_str = input("Enter your move (e.g., e2e4): ")
            move = chess.Move.from_uci(move_str)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid move format! Try again.")

# Function to get the AI's move using Stockfish
def get_ai_move(board, difficulty_level):
    # Set the desired search depth based on the difficulty level
    if difficulty_level == "easy":
        search_depth = 2
    elif difficulty_level == "medium":
        search_depth = 4
    elif difficulty_level == "hard":
        search_depth = 6
    elif difficulty_level == "very hard":
        search_depth = 8
    elif difficulty_level == "expert":
        search_depth = 10
    else:
        # Default to medium difficulty
        search_depth = 4

    stockfish_path = "stockfish"  # Replace this with the path to Stockfish executable if needed

    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        result = engine.play(board, chess.engine.Limit(depth=search_depth))
        return result.move

# Main game loop with AI difficulty setting
def play_game():
    board = chess.Board()

    difficulty_level = input("Choose AI difficulty (easy, medium, hard, very hard, expert): ").lower()

    # Display the initial board before the game starts
    print("\nInitial Board:")
    print(display_board(board))

    while not board.is_game_over():
        # Get player's move
        player_move = get_player_move(board)
        board.push(player_move)
        print("\nPlayer's Move:")
        print(display_board(board))

        if board.is_game_over():
            break

        # Get AI's move with the specified difficulty level
        ai_move = get_ai_move(board, difficulty_level)
        board.push(ai_move)
        print("\nAI's Move:")
        print(display_board(board))

    print("Game Over!")
    print("Result:", board.result())

# Start the game
if __name__ == "__main__":
    play_game()

