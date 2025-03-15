class Solution(object):
    def subsetsWithDup(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        nums.sort()  # Step 1: Sort to handle duplicates
        result = []

        def backtrack(start, path):
            result.append(path[:])  # Add the current subset

            for i in range(start, len(nums)):
                # Step 3: Skip duplicate elements
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result