# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        \\\
        inorder_nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Identify the two swapped nodes
        first, second = None, None
        for i in range(len(inorder_nodes) - 1):
            if inorder_nodes[i].val > inorder_nodes[i + 1].val:
                if not first:
                    first = inorder_nodes[i]  # First incorrect node
                second = inorder_nodes[i + 1]  # Last incorrect node

        # Step 3: Swap values
        first.val, second.val = second.val, first.val