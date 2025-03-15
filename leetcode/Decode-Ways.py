class Solution(object):
    def numDecodings(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        if not s or s[0] == '0':  # If starts with '0', it's invalid
            return 0
        
        prev, curr = 1, 1  # dp[i-2] and dp[i-1]
        
        for i in range(1, len(s)):
            temp = 0
            
            if s[i] != '0':  # Single digit (1-9)
                temp += curr

            if 10 <= int(s[i-1:i+1]) <= 26:  # Two-digit (10-26)
                temp += prev
            
            prev, curr = curr, temp  # Update previous values
        
        return curr