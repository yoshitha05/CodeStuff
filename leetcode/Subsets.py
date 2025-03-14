class Solution(object):
    def subsets(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
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