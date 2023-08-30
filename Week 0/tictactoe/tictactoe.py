"""
Tic Tac Toe Player
"""

import math
import copy

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
    count = 0
    for row in board:
        for cell in row:
            if cell == X:
                count += 1
            elif cell == O:
                count -= 1
    
    return X if count == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                actions.append((row, column))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Action")
    else:
        new_board[action[0]][action[1]] = player(new_board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    for i in (0, 2):
        if board[i][0] == board[1][1] == board[abs(i - 2)][2]:
            return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or all(EMPTY not in row for row in board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)
    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current = player(board)
    
    if current == X:
        best_action = highest_score(board)[1]
    else:
        best_action = lowest_score(board)[1]

    return best_action


def highest_score(board):
    possible_actions = actions(board)
    score = float('-inf')
    best_action = None

    for action in possible_actions:
        new_board = result(board, action)
        if terminal(new_board):
            new_score = utility(new_board)
        else:
            new_score = lowest_score(new_board)[0]

        if new_score > score:
            score, best_action = new_score, action
    
    return score, best_action


def lowest_score(board):
    possible_actions = actions(board)
    score = float('inf')
    best_action = None

    for action in possible_actions:
        new_board = result(board, action)
        if terminal(new_board):
            new_score = utility(new_board)
        else:
            new_score = highest_score(new_board)[0]

        if new_score < score:
            score, best_action = new_score, action
    
    return score, best_action
