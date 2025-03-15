class Solution(object):
    def numTrees(self, n):
        \\\
        :type n: int
        :rtype: int
        \\\
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base cases

        for nodes in range(2, n + 1):  # Compute up to n
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]  # Use formula
        
        return dp[n]