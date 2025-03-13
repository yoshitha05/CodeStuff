class Solution(object):
    def rotate(self, matrix):
        \\\
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        \\\
        n = len(matrix)

        # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()