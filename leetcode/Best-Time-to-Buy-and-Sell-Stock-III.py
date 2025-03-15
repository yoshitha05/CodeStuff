class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        if not prices:
            return 0
        
        first_buy = float('inf')
        first_profit = 0
        second_buy = float('inf')
        second_profit = 0
        
        for price in prices:
            first_buy = min(first_buy, price)  # Minimum price for first buy
            first_profit = max(first_profit, price - first_buy)  # Max profit after first sell
            second_buy = min(second_buy, price - first_profit)  # Minimum effective cost for second buy
            second_profit = max(second_profit, price - second_buy)  # Max profit after second sell
            
        return second_profit