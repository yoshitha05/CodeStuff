class Solution(object):
    def uniquePaths(self, m, n):
        \\\
        :type m: int
        :type n: int
        :rtype: int
        \\\
        dp = [[1] * n for _ in range(m)]  

        for i in range(1, m):  # Start from row 1
            for j in range(1, n):  # Start from column 1
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # Sum of top & left cells

        return dp[m - 1][n - 1]  # Return bottom-right value