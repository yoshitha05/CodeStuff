# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        \\\
        :type n: int
        :rtype: List[Optional[TreeNode]]
        \\\
        if n == 0:
            return []
        
        def build_trees(start, end):
            if start > end:
                return [None]  # Base case: Empty subtree
            
            all_trees = []
            for i in range(start, end + 1):  # Choose `i` as root
                left_trees = build_trees(start, i - 1)   # Generate all left subtrees
                right_trees = build_trees(i + 1, end)    # Generate all right subtrees

                # Combine left and right trees with root `i`
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i, left, right)
                        all_trees.append(root)
            
            return all_trees
        
        return build_trees(1, n)