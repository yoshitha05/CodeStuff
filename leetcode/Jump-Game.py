class Solution(object):
    def canJump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        max_reachable = 0
        for i, num in enumerate(nums):
            if i > max_reachable:
                return False  # If we reach an index beyond max_reachable, we can't continue
            max_reachable = max(max_reachable, i + num)  # Update max reachable index
            if max_reachable >= len(nums) - 1:
                return True  # If we can reach the last index, return True
        
        return max_reachable >= len(nums) - 1