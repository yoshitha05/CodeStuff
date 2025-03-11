class Solution(object):
    def maxArea(self, height): 
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1  # Initialize the two pointers
        max_water = 0  # Variable to track maximum area

        while left < right:
            # Calculate the current area
            min_height = min(height[left], height[right])
            width = right - left
            max_water = max(max_water, min_height * width)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water 
