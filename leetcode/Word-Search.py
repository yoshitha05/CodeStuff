class Solution(object):
    def exist(self, board, word):
        \\\
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        \\\
        result = []
        
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return result
    
    def subsets(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        result = []
        
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result
    
    def exist(self, board, word):
        \\\
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        \\\
        if not board:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'  # Mark as visited
            
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            board[r][c] = temp  # Unmark
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False