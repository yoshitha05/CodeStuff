class Solution(object):
    def minWindow(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: str
        \\\
        if not s or not t:
            return \\
        
        t_count = Counter(t)
        current_count = {}
        required = len(t_count)
        formed = 0
        left, right = 0, 0
        min_len = float(\inf\)
        min_window = \\
        
        while right < len(s):
            char = s[right]
            current_count[char] = current_count.get(char, 0) + 1
            
            if char in t_count and current_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]
                
                left_char = s[left]
                current_count[left_char] -= 1
                if left_char in t_count and current_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return min_window

# Example Usage
solution = Solution()
print(solution.minWindow(\ADOBECODEBANC\, \ABC\))  # Output: \BANC\
print(solution.minWindow(\a\, \a\))  # Output: \a\
print(solution.minWindow(\a\, \aa\))  # Output: \\
