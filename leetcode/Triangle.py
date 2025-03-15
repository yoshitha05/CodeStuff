class Solution(object):
    def minimumTotal(self, triangle):
        \\\
        :type triangle: List[List[int]]
        :rtype: int
        \\\
        n = len(triangle)
        dp = triangle[-1][:]  # Start with the last row

        # Bottom-up computation
        for row in range(n - 2, -1, -1):
            for col in range(row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]