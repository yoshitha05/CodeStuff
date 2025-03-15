# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        \\\
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True  # Direction flag
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Append based on direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)  # Reverse order
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            left_to_right = not left_to_right  # Toggle direction
        
        return result