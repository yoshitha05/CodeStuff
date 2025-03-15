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
            
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:  # Connect current node to next node in the level
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root