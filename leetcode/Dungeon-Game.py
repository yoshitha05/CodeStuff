class Solution(object):
    def calculateMinimumHP(self, dungeon):
        \\\
        :type dungeon: List[List[int]]
        :rtype: int
        \\\
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_hp_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_hp_on_exit - dungeon[i][j])

        return dp[0][0]
