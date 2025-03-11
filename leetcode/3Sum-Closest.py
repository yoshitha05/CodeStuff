class Solution(object):
    def threeSumClosest(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: int
        \\\
        nums.sort()  # Step 1: Sort the array
        closest_sum = float('inf')  # Initialize with a large number
        
        for i in range(len(nums) - 2):  # Fix one element
            left, right = i + 1, len(nums) - 1  # Two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if this is closer to the target
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total
                
                if total < target:
                    left += 1  # Move left pointer to increase sum
                elif total > target:
                    right -= 1  # Move right pointer to decrease sum
                else:
                    return total  # Exact match, return immediately
        
        return closest_sum
