class Solution:
    def rob(self, nums):
        prev_max, curr_max = 0, 0
        for num in nums:
            prev_max, curr_max = curr_max, max(curr_max, prev_max + num)
        return curr_max
