class Solution(object):
    def simplifyPath(self, path):
        \\\
        :type path: str
        :rtype: str
        \\\
        stack = []
        parts = path.split(\/\)  # Split by '/'
        
        for part in parts:
            if part == \..\:  # Go back to parent directory
                if stack:
                    stack.pop()
            elif part and part != \.\:  # Ignore empty and current directory '.'
                stack.append(part)
        
        return \/\ + \/\.join(stack)