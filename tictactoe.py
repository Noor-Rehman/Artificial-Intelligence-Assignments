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
    X_Count=sum(row.count("X") for row in board)
    Y_Count=sum(row.count("O") for row in board)
    if X_Count<=Y_Count:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is None}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    if board[i][j] is not None:
        raise ValueError("Invalid Move")
    new_board=[row[:] for row in board]
    current_player=player(board)
    new_board[i][j]=current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for symbol in ["X","O"]:
        for i in range(3):
            if all(board[i][j]==symbol for j in range(3)) or all(board[j][i]==symbol for j in range(3)):
                return symbol
        if all(board[d][d]==symbol for d in range(3)) or all(board[d][2-d]==symbol for d in range(3)):
            return symbol
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell is not None for cell in row) for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Winner_of_Game=winner(board)
    if Winner_of_Game=="X":
        return 1
    elif Winner_of_Game=="O":
        return -1
    else:
        return 0


def minimax(board,alpha=-math.inf,beta=math.inf):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player=player(board)

    def max_value(state,alpha,beta):
        if terminal(state):
            return utility(state)
        v=-math.inf
        for action in actions(state):
            v=max(v,min_value(result(state,action),alpha,beta))
            alpha=max(alpha,v)
            if alpha>=beta:
                break
        return v
    def min_value(state,alpha,beta):
        if terminal(state):
            return utility(state)
        v=math.inf
        for action in actions(state):
            v=min(v,max_value(result(state,action),alpha,beta))
            beta=min(beta,v)
            if alpha>=beta:
                break
        return v 
    best_action=None
    if current_player=="X":
        best_value=-math.inf
        for action in actions(board):
            value=min_value(result(board,action),alpha,beta)
            if value>best_value:
                best_value=value
                best_action=action
            alpha=max(alpha,best_value)
    else:
        best_value=math.inf
        for action in actions(board):
            value=max_value(result(board,action),alpha,beta)
            if value<best_value:
                best_value=value
                best_action=action
            beta=min(beta,best_value)
        
    return best_action