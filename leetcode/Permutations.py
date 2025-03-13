class Solution(object):
    def permute(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        res = []
        
        def backtrack(path, remaining):
            if not remaining:  # If no numbers left to pick
                res.append(path)
                return
            
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return res