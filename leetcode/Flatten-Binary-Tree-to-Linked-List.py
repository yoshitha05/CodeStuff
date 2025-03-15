# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        \\\
        self.prev = None  # Track the previous node in traversal

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)  # Process right subtree first
            dfs(node.left)   # Process left subtree
            
            node.right = self.prev  # Update right child
            node.left = None        # Set left child to None
            self.prev = node        # Update previous node
        
        dfs(root)