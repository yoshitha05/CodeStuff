class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        min_num, max_num = min(nums), max(nums)
        gap = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_count = (max_num - min_num) // gap + 1
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        for num in nums:
            if num == min_num or num == max_num:
                continue
            idx = (num - min_num) // gap
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        max_gap = float('-inf')
        prev_max = min_num
        for i in range(bucket_count):
            if buckets[i][0] == float('inf'):
                continue
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
        
        max_gap = max(max_gap, max_num - prev_max)
        
        return max_gap
