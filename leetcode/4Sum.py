class Solution(object):
    def fourSum(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        \\\
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for i
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate values for j
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif total < target:
                        left += 1  # Move left pointer to increase sum
                    else:
                        right -= 1  # Move right pointer to decrease sum
         
        return result
