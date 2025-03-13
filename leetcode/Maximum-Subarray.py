class Solution(object):
    def maxSubArray(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        max_sum = float('-inf')  # Initialize max_sum to smallest possible value
        curr_sum = 0  # Tracks the current subarray sum

        for num in nums:
            curr_sum = max(num, curr_sum + num)  # Either start new subarray or extend existing one
            max_sum = max(max_sum, curr_sum)  # Update max_sum if needed

        return max_sum