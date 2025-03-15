class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        min_price = float('inf')  # Track the minimum price
        max_profit = 0  # Track the maximum profit

        for price in prices:
            min_price = min(min_price, price)  # Update minimum price
            max_profit = max(max_profit, price - min_price)  # Update max profit

        return max_profit