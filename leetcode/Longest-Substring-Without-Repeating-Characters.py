class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # Dictionary to store the index of characters
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Maximum length of substring without repeating characters

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # Move left pointer past the repeated character
            
            char_index[s[right]] = right  # Update character index
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
         
