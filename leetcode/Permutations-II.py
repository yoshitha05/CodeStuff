class Solution(object):
    def permuteUnique(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        res = []
        nums.sort()  # Sorting helps in skipping duplicates
        used = [False] * len(nums)  # Track used elements

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])  # Append a copy of path
                return
            
            for i in range(len(nums)):
                # Skip used elements or duplicates
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()  # Undo the choice
                used[i] = False

        backtrack([])
        return res