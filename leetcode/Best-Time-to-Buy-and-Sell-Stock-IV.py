class Solution(object):
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for transaction in range(1, k + 1):
            max_diff = -prices[0]
            for day in range(1, n):
                dp[day][transaction] = max(dp[day - 1][transaction], prices[day] + max_diff)
                max_diff = max(max_diff, dp[day][transaction - 1] - prices[day])
        
        return dp[n - 1][k]