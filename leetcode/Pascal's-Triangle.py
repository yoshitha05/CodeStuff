class Solution(object):
    def generate(self, numRows):
        \\\
        :type numRows: int
        :rtype: List[List[int]]
        \\\
        result = [[1]]  # First row

        for i in range(1, numRows):
            prev_row = result[-1]
            cur_row = [1]  # Start with 1

            # Compute middle elements
            for j in range(1, i):
                cur_row.append(prev_row[j - 1] + prev_row[j])

            cur_row.append(1)  # End with 1
            result.append(cur_row)

        return result 