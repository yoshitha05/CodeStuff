class Solution(object):
    def getRow(self, rowIndex):
        \\\
        :type rowIndex: int
        :rtype: List[int]
        \\\
        row = [1] * (rowIndex + 1)  # Initialize row with all 1s

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        
        return row