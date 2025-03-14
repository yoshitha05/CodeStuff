class Solution(object):
    def setZeroes(self, matrix):
        \\\
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        \\\
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set elements to zero using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Update first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Update first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# Example Usage
solution = Solution()
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution.setZeroes(matrix2)
print(matrix2)  # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]