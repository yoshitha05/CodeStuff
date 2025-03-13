class Solution(object):
    def trap(self, height):
        \\\
        :type height: List[int]
        :rtype: int
        \\\
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    water_trapped += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    water_trapped += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
         
        return water_trapped
