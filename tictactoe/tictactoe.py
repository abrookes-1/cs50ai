"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]   


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0
    for row in board:
        for square in row:
            if square == X:
                num_x += 1
            elif square == O:
                num_o += 1
    
    if num_x > num_o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                actions.append((row, col))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    board[row][col] = player(board)

    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows for winner
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]
        
    # check cols for winner
    for col in board:
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return board[0][col]
    
    # check diagonals for winner
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        for square in row:
            if square is None:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if X == won:
        return 1
    if O == won:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
