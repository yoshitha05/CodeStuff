class Solution(object):
    def combinationSum2(self, candidates, target):
        \\\
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        res = []
        candidates.sort()  # Sorting helps in skipping duplicates

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            prev = -1  # To track duplicate elements
            for i in range(start, len(candidates)):
                if candidates[i] == prev:  # Skip duplicates
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # i + 1 ensures no reuse
                path.pop()  # Undo the choice
                prev = candidates[i]  # Mark this element to skip in the next loop iteration

        backtrack(0, [], 0)
        return res 
