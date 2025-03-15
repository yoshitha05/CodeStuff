class Solution(object):
    def minCut(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        n = len(s)
        dp = [float('inf')] * n
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or pal[j + 1][i - 1]):
                    pal[j][i] = True

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]