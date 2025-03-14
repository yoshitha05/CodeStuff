class Solution(object):
    def combine(self, n, k):
        \\\
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        \\\
        result = []
        
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return result

# Example Usage
solution = Solution()
print(solution.combine(4, 2))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(solution.combine(1, 1))