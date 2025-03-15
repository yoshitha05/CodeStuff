class Solution(object):
    def numDistinct(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: int
        \\\
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1  # An empty t can always be formed
        
        for i in range(1, m + 1):
            prev = dp[:]  # Copy previous row
            for j in range(n, 0, -1):  # Reverse to prevent overwriting
                if s[i - 1] == t[j - 1]:
                    dp[j] += prev[j - 1]  # Include current character

        return dp[n]