class Solution(object):
    def totalNQueens(self, n):
        \\\
        :type n: int
        :rtype: int
        \\\
        def solve(row, cols, diag1, diag2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                count += solve(row + 1, cols, diag1, diag2)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            return count
        
        return solve(0, set(), set(), set())