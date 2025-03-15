# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        \\\
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.insert(0, level)  # Insert at the beginning for bottom-up order
        
        return result