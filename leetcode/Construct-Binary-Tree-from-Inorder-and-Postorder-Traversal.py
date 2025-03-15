# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        \\\
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        \\\
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # Store inorder indices
        self.post_idx = len(postorder) - 1  # Start from the last index of postorder
        
        def construct(left, right):
            if left > right:
                return None
            
            root_val = postorder[self.post_idx]  # Pick root from postorder (last element)
            root = TreeNode(root_val)
            self.post_idx -= 1  # Move to the next root in postorder
            
            # Find index of root in inorder traversal
            inorder_idx = inorder_map[root_val]
            
            # Build right subtree first (since we traverse postorder from the end)
            root.right = construct(inorder_idx + 1, right)
            root.left = construct(left, inorder_idx - 1)
            
            return root
        
        return construct(0, len(inorder) - 1)