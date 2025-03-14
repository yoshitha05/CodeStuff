class Solution(object):
    def merge(self, intervals):
        \\\
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        \\\
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]  # Initialize with the first interval

        for i in range(1, len(intervals)):
            prev = merged[-1]  # Last merged interval
            curr = intervals[i]  # Current interval

            if curr[0] <= prev[1]:  
                # Merge overlapping intervals
                prev[1] = max(prev[1], curr[1])
            else:
                # No overlap, add to result
                merged.append(curr)

        return merged