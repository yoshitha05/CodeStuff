class Solution(object):
    def isMatch(self, s, p):
        \\\
        :type s: str
        :type p: str
        :rtype: bool
        \\\
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Fill first row (pattern matching empty string)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*': 
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[m][n]
