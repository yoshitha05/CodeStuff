# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        \\\
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        \\\
        if not root:
            return False  # Empty tree has no path
        
        # Subtract the current node's value from targetSum
        targetSum -= root.val
        
        # If we reached a leaf and targetSum is 0, return True
        if not root.left and not root.right:
            return targetSum == 0
        
        # Recursively check left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)