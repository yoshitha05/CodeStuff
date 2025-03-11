class Solution(object):
    def removeElement(self, nums, val):
        \\\
        :type nums: List[int]
        :type val: int
        :rtype: int
        \\\
        i = 0  # Slow pointer for placement of non-val elements
        for j in range(len(nums)):  # Fast pointer to scan elements
            if nums[j] != val:
                nums[i] = nums[j]  # Place the non-val element at index i
                i += 1  # Move the slow pointer forward 
        return i  # New length of modified array
