\\\
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
\\\

class Solution(object):
    def connect(self, root):
        \\\
        :type root: Node
        :rtype: Node
        \\\
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            prev = None  # Tracks the previous node in the level
            
            for _ in range(size):
                node = queue.popleft()
                
                if prev:
                    prev.next = node  # Connect previous node to current
                
                prev = node  # Move prev to current node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            prev.next = None  # Ensure last node in the level points to NULL

        return root