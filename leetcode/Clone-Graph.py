\\\
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
\\\

class Solution(object):
    def cloneGraph(self, node):
        \\\
        :type node: Node
        :rtype: Node
        \\\
        if not node:
            return None
        
        cloned_nodes = {}

        def clone(node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            new_node = Node(node.val)
            cloned_nodes[node] = new_node
            
            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))
            
            return new_node

        return clone(node)
