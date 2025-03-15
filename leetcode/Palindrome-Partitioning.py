class Solution(object):
    def partition(self, s):
        \\\
        :type s: str
        :rtype: List[List[str]]
        \\\
        res = []  # Stores all valid palindrome partitions
        path = []  # Stores the current partition
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start):
            if start == len(s):  # Base case: reached the end of the string
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if is_palindrome(sub):  # Check if the substring is a palindrome
                    path.append(sub)  # Choose
                    backtrack(end+1)  # Explore
                    path.pop()  # Unchoose (backtrack)
        
        backtrack(0)
        return res