class Solution(object):
    def isScramble(self, s1, s2):
        \\\
        :type s1: str
        :type s2: str
        :rtype: bool
        \\\
        memo = {}

        def solve(s1, s2):
            if s1 == s2:
                return True
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            if sorted(s1) != sorted(s2):  # Quick rejection if characters don't match
                memo[(s1, s2)] = False
                return False
            
            n = len(s1)
            for i in range(1, n):  # Try every possible split
                # Case 1: No swap
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # Case 2: Swap
                if solve(s1[:i], s2[-i:]) and solve(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True
            
            memo[(s1, s2)] = False
            return False
        
        return solve(s1, s2)