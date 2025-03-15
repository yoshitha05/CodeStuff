class Solution(object):
    def solve(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        \\\
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = '#'  # Mark as safe
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Step 1: Mark border-connected 'O's
        for i in range(rows):
            dfs(i, 0)  # Left border
            dfs(i, cols - 1)  # Right border
        for j in range(cols):
            dfs(0, j)  # Top border
            dfs(rows - 1, j)  # Bottom border
        
        # Step 2: Modify board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':  # Surrounded region
                    board[i][j] = 'X'
                elif board[i][j] == '#':  # Border-connected region
                    board[i][j] = 'O'