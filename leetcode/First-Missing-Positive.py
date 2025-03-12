class Solution(object):
    def firstMissingPositive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        n = len(nums)
        
        # Step 1: Place each number in its correct index (Cyclic Sort)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap
        
        # Step 2: Identify the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers are in place, return the next number
        return n + 1 
