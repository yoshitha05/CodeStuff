# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: bool
        \\\
        def is_valid(node, min_val, max_val):
            if not node:
                return True  # Empty trees are valid
            
            if not (min_val < node.val < max_val):
                return False  # Node violates BST property
            
            return (is_valid(node.left, min_val, node.val) and
                    is_valid(node.right, node.val, max_val))
        
        return is_valid(root, float('-inf'), float('inf'))