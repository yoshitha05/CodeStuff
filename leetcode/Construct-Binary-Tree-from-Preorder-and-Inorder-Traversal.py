# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        \\\
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        \\\
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # Store inorder indices
        self.pre_idx = 0  # Preorder index tracker
        
        def construct(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1  # Move to the next preorder index
            
            # Get inorder index of the current root
            inorder_idx = inorder_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = construct(left, inorder_idx - 1)
            root.right = construct(inorder_idx + 1, right)
            
            return root
        
        return construct(0, len(inorder) - 1)