class Solution(object):
    def insert(self, intervals, newInterval):
        \\\
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        \\\
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)  # Add the merged interval

        # Step 3: Add the remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result