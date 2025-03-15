# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: int
        \\\
        def dfs(node, curr_num):
            if not node:
                return 0
            
            curr_num = curr_num * 10 + node.val  # Update current number
            
            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return curr_num
            
            # Recur for left and right subtrees
            return dfs(node.left, curr_num) + dfs(node.right, curr_num)

        return dfs(root, 0)