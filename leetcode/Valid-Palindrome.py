class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Step 2: Use two-pointer technique
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False  # Not a palindrome
            left += 1
            right -= 1
        
        return True  # It is a palindrome