"""
Tic Tac Toe Player
"""

import math
import copy
import random


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

def isfirstmove(board):

    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                return False

    return True


"""
Returns player who has the next turn on a board.
"""
def player(board):

    countx = 0
    counto = 0

    for row in board:
        for cell in row:
            if cell == X:
                countx += 1
            if cell == O:
                counto +=1

    if (counto + countx) % 2 == 0:
        return X

    return O


"""
Returns set of all possible actions (i, j) available on the board.
"""
def actions(board):

    available = set()
    counteri = -1

    for i in board:
        counteri +=1
        counterj = -1
        for j in i:
            counterj +=1
            if j == EMPTY:
                available.add((counteri,counterj))
    
    return available


"""
Returns the board that results from making move (i, j) on the board.
"""
def result(board, action):

    plr = player(board)

    #copying the board so we don't change the original
    copy_board = copy.deepcopy(board)

    #searching for the right place to place the player play
    for i in range(3):
        if i == action[0]:
            for j in range(3):
                if j == action[1]:
                    if board[i][j] != EMPTY:
                        raise Exception("Invalid move")
                    else:
                        copy_board[i][j] = plr
    
    return copy_board


"""
Returns the board where +1 is X, -1 is O and 0 is EMPTY.
"""
def change(board):

    copy_board = []
    for i in range(3):
        row = []
        for j in range(3):
            if board[i][j] == X:
                row.append(+1)
            elif board[i][j] == O:
                row.append(-1)
            else:
                row.append(0)
        copy_board.append(row)

    return copy_board


"""
Returns the winner of the game, if there is one.
"""
def winner(board):

    new_board = change(board)

    #Checks for row sums
    for row in new_board:
        soma = sum(row)
        if soma == -3:
            return O
        if soma == 3:
            return X

    #Checks for primary diagonal sum
    diag = sum(new_board[i][i] for i in range(3)) 
    if diag == -3:
        return O
    if diag == 3:
        return X

    #Checks for secondary diagonal sum
    diag_sec = sum(new_board[i][2-i] for i in range(3))
    if diag_sec == -3:
        return O
    if diag_sec == 3:
        return X
    
    #Checks for column sums
    for j in range(3):
        col = sum(new_board[i][j] for i in range(3))
        if col == -3:
            return O
        if col == 3:
            return X

    return False


"""
Returns True if game is over, False otherwise.
"""
def terminal(board):

    if winner(board) is not False:
        return True
    elif sum(row.count(EMPTY) for row in board) == 0:
        return True
    else:
        return False


"""
Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
"""
def utility(board):

    n = winner(board)
    if n == X:
        return 1
    elif n == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    nextplayer = player(board)

    if nextplayer == X:
        possibx = {}
        for action in actions(board):
            possibx[action] = max_value(result(board, action))    
        return max(possibx, key=possibx.get)

    if nextplayer == O:
        possibo = {}
        for action in actions(board):
            possibo[action] = min_value(result(board, action))
        return min(possibo, key=possibo.get)
 
def max_value(board):
    
    if terminal(board):
        return utility(board)
    
    v = float('-inf') 

    for action in actions(board):
        v = max(v, min_value(result(board,action)))

    return v

def min_value(board):

    if terminal(board):
        return utility(board) 

    v = float('inf')

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v
