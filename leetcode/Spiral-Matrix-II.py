class Solution(object):
    def generateMatrix(self, n):
        \\\
        :type n: int
        :rtype: List[List[int]]
        \\\
        matrix = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with zeros
        left, right, top, bottom = 0, n - 1, 0, n - 1  # Define boundaries
        num = 1  # Start filling numbers from 1 to n^2
        
        while left <= right and top <= bottom:
            # Move from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move down the top boundary
            
            # Move from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move left the right boundary
            
            # Move from right to left
            if top <= bottom:  # Ensure valid row
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # Move up the bottom boundary
            
            # Move from bottom to top
            if left <= right:  # Ensure valid column
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # Move right the left boundary

        return matrix