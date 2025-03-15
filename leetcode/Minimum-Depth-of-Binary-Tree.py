# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: int
        \\\
        if not root:
            return 0  # Base case: Empty tree has depth 0
        
        # If one child is None, return the depth of the other child + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both children exist, take the min depth of both + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1