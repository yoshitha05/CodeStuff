class Solution(object):
    def solveNQueens(self, n):
        \\\
        :type n: int
        :rtype: List[List[str]]
        \\\
        def is_safe(board, row, col):
            # Check vertical column
            for i in range(row):
                if board[i] == col:
                    return False
            # Check left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i] == j:
                    return False
            # Check right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i] == j:
                    return False
            return True

        def solve(row, board):
            if row == n:
                result.append([\.\ * c + \Q\ + \.\ * (n - c - 1) for c in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
                    board[row] = -1

        result = []
        board = [-1] * n  # Store queen positions
        solve(0, board)
        return result