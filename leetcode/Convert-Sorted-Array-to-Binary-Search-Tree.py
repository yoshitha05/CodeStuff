# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        \\\
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        \\\
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # Middle element as root
        
        root.left = self.sortedArrayToBST(nums[:mid])  # Left subarray -> Left subtree
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Right subarray -> Right subtree
        
        return root