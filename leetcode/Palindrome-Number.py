class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reversing half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # A number is a palindrome if the original number (or the truncated half)
        # matches the reversed half
        return x == reversed_half or x == reversed_half // 10
    
