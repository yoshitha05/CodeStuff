class Solution(object):
    def largestRectangleArea(self, heights):
        \\\
        :type heights: List[int]
        :rtype: int
        \\\
        stack = []  # Stores indices of histogram bars
        max_area = 0  # Maximum area found
        heights.append(0)  # Sentinel value to ensure all bars are processed

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area