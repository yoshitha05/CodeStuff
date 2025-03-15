class Solution(object):
    def maximalRectangle(self, matrix):
        \\\
        :type matrix: List[List[str]]
        :rtype: int
        \\\
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols  # Histogram heights
        max_area = 0
        
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Sentinel to ensure all bars are processed
            
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            
            heights.pop()  # Remove the sentinel value
            return max_area

        for row in matrix:
            for col in range(cols):
                heights[col] = heights[col] + 1 if row[col] == \1\ else 0
            
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area