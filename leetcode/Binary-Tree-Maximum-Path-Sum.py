# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        \\\
        :type root: TreeNode
        :rtype: int
        \\\
        self.max_sum = float('-inf')  # Stores the maximum path sum found

        def dfs(node):
            if not node:
                return 0  # Base case: If node is None, return 0
            
            # Recursively get max path sum of left and right subtrees
            left_max = max(dfs(node.left), 0)  # Ignore negative sums
            right_max = max(dfs(node.right), 0)

            # Compute the max path sum including current node as root
            current_sum = node.val + left_max + right_max
            
            # Update global max sum
            self.max_sum = max(self.max_sum, current_sum)

            # Return max path sum that can be extended upwards
            return node.val + max(left_max, right_max)

        dfs(root)  # Start DFS from the root
        return self.max_sum  # Return the maximum path sum found
