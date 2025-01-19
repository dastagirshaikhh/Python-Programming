# Practical 12
# Program to implement N-Queen Problem, Binary String
# generation using Backtracking Strategy
def n_queen(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            res.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    res = []
    board = [-1] * n
    backtrack(board, 0)
    return res


print(n_queen(4))