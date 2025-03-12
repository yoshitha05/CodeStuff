class Solution(object):
    def combinationSum(self, candidates, target):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        res = []

        def backtrack(start, path, total): 
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # Not i + 1 because we can reuse the same element
                path.pop()  # Undo the choice

        backtrack(0, [], 0)
        return res
