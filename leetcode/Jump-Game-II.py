class Solution(object):
    def jump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        n = len(nums)
        if n == 1:
            return 0  # No jumps needed if already at the end
        
        jumps, current_end, farthest = 0, 0, 0
        
        for i in range(n - 1):  # Stop at n-1 since last index is our goal
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:  # Need a jump to move further
                jumps += 1
                current_end = farthest
            
            if current_end >= n - 1:  # If we can reach the end, stop early
                return jumps
        
        return jumps