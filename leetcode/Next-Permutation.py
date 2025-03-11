class Solution(object):
    def nextPermutation(self, nums):
        \\\
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        \\\
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # If we found a valid index
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 2: Swap nums[i] with nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the sequence to the right of i
        nums[i + 1:] = reversed(nums[i + 1:])