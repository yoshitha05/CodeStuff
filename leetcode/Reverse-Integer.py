class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits of the integer
        reversed_x = int(str(x)[::-1])
        
        # Reapply the sign
        reversed_x *= sign
        
        # Handle overflow for 32-bit signed integers
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x
