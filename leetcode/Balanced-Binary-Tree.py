# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: bool
        \\\
        def check_height(node):
            if not node:
                return 0  # Base case: height of empty tree is 0
            
            left_height = check_height(node.left)
            right_height = check_height(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1  # If unbalanced, return -1 immediately
            
            return max(left_height, right_height) + 1  # Return height
        
        return check_height(root) != -1