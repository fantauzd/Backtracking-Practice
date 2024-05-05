# N-Queens Problem: The problem is to place N queens on an NxN chessboard such that no two queens
# are attacking each other. According to the rules of chess, a queen can be attacked horizontally,
# vertically and diagonally. The below figure shows the attacking positions of a queen.

def n_Queens(N):
    '''
    Returns an NxN board with N-queens placed in correct positions.
    '''
    board = [[0 for x in range(N)] for x in range(N)]
    solve_n_Queens(board, 0, N, N)
    return board

def solve_n_Queens(board, row, N, remaining):
    """
    Solves the n queens problem.
    :param board: a 2d array representing a chess board
    :param row: int, The row we are trying to place a queen in, each row must support 1 queen.
    :param N: int, The number of queens to be placed
    :param remaining: int, The number of queens we have left to place
    :return: boolean
    """
    if remaining == 0:
        return True         # base case
    for column in range(N):
        # skip cells that are attacked
        if not is_attacked(row, column, board, N):
            # Place the queen and recursively solve for remaining queens
            board[row][column] = 1
            if(solve_n_Queens(board, row+1, N, remaining-1)):
                return True
            #backtrack if any placement results in no solution
            board[row][column] = 0
    return False


def is_attacked(row, column, board, N):
    # check row
    for i in range(N):
        if board[row][i] == 1:
            return True
    # check column
    for j in range(N):
        if board[j][column] == 1:
            return True
    # check diagonal
    for p in range(1, N):
        # check NW
        if column - p >= 0 and row - p >= 0:
            if board[row-p][column-p] == 1:
                return True
        # check NE
        if column - p >= 0 and row + p >= 0:
            if board[row-p][column+p] == 1:
                return True
        # check SE
        if column + p >= 0 and row + p >= 0:
            if board[row+p][column+p] == 1:
                return True
        # check SW
        if column + p >= 0 and row - p >= 0:
            if board[row+p][column-p] == 1:
                return True


if __name__ == "__main__":
    print(n_Queens(3))