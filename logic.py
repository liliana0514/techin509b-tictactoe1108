def check_winner(board):
    # check rows
    #    ['X', 'X', 'X'], -> set(['X', 'X', 'X']) -> {'X'}
    #    ['O', 'X', 'O'], -> set(['O', 'X', 'O']) -> {'X', 'O'}
    #    ['O', 'O', 'X'],
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # column_idxs = [[0,0], [1,0], [2,0]]
    # column_idxs = [[0,1], [1,1], [2,1]]
    for i in range(len(board)):
        # len(board) -> 3
        column = [board[j][i] for j in range(len(board))]
        # column => ['X', 'O', 'O']
        # column => ['X', 'X', 'O]
        if len(set(column)) == 1:
            return board[0][i]

    # check diagonals
    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # idx -> [[0,0], [1,1], [2, 2]]
    top_left_to_bottom_right = [board[i][i] for i in range(len(board))]
    if len(set(top_left_to_bottom_right)) == 1:
        return board[0][0]

    # check diagonals
    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # idx -> [[0,2], [1,1], [2, 0]]
    top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(top_right_to_bottom_left)) == 1:
        return board[0][len(board)-1]

    # Check draw
    """
    board = [
        ['O', None, None],
        [None, None, None],
        [None, 'X', None],
    ]

    board = [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'X', 'O'],
    ]
    """

    # [2,2].append([1,1]) -> [2,2, [1,1]]
    # [2,2].extend([1,1]) -> [2,2,1,1] 
    # flat_board = ["O", "X", "O","O", "X", "O","O", "X", "O"]
    flat_board = []
    for row in board:
        flat_board.extend(row)
    if not None in flat_board:
        return "draw"

    # game still in play
    return None

if __name__ == "__main__":
    board = [
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "X", "O"],
    ]
    print(check_winner(board))


def get_empty_board():
    """
    row_1 = ['O', 'O', 'O']
    row_2 = ['O', 'O', 'O']
    row_3 = ['O', 'O', 'O']

    board = [row_1, row_2, row_3]
    """
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def print_board(board):
    for row in board:
        print(row)  # print will print the variable in a new line


def get_player_input(player_input):
    """
    input:
        row,col
    return:
        row: int -> the index of row
        col: int -> the index of column
    """
    row_col_list = player_input.split(",")  # ["1", "1"]
    row, col = [int(x) for x in row_col_list]  # [1,1]
    return row, col


def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"
