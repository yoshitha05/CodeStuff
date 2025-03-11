class Solution(object):
    def letterCombinations(self, digits):
        \\\
        :type digits: str
        :rtype: List[str]
        \\\
        if not digits:
            return []
        
        phone_map = {
            \2\: \abc\, \3\: \def\, \4\: \ghi\, \5\: \jkl\,
            \6\: \mno\, \7\: \pqrs\, \8\: \tuv\, \9\: \wxyz\
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):  # Base case: if we reach the end of digits
                result.append(\\.join(path))
                return
            
            # Get possible letters for the current digit
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                path.append(letter)  # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()  # Un-choose (backtrack)
        
        backtrack(0, [])  # Start backtracking from index 0
        return result 
