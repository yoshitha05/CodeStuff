class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        if not nums:
            return 0

        numSet = set(nums)  # Store numbers in a set for O(1) lookups
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:  # Start counting only if it's the beginning of a sequence
                length = 1
                while num + length in numSet:
                    length += 1  # Expand the sequence

                longest = max(longest, length)  # Update longest sequence

        return longest