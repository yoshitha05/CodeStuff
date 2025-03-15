# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        \\\
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        \\\
        if not p and not q:  # Both trees are empty
            return True
        if not p or not q:  # One tree is empty, the other is not
            return False
        if p.val != q.val:  # Values at current nodes differ
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)