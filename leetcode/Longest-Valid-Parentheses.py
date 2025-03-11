class Solution(object):
    def longestValidParentheses(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        stack = [-1]  # Initialize stack with -1 for base case
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop previous '(' or invalid ')'
                if not stack:
                    stack.append(i)  # Push current index as new invalid base
                else:
                    max_length = max(max_length, i - stack[-1])  # Compute max length
        
        return max_length 
