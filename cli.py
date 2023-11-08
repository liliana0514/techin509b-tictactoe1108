# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.


from logic import check_winner, get_empty_board, print_board, get_player_input, switch_player

if __name__ == "__main__":
    current_player = "X"
    board = get_empty_board()  # get a empty board
    winner = None

    while winner is None:
        print_board(board)  # print the board
        player_input = input(f"player {current_player} > ")
        try:
            row, col = get_player_input(player_input)  # ask user input
        except ValueError:
            print("Invalid input, try again\n")
            continue

        if row >= len(board[0]) or col >= len(board):
            print(f"Out of bounds, try again\n")
            continue

        if board[row][col]:
            print(
                f"{row},{col} already has mark {board[row][col]}, please choose another place\n"
            )
            continue

        # mark the board
        board[row][col] = current_player

        # check for winner
        winner = check_winner(board)  # "O", "X" -> break out of the loop

        current_player = switch_player(current_player)
        print("\n")
        # current_player = "X" if current_player == "O" else "O"
    print_board(board)
    print(f"Winner is {winner}")
