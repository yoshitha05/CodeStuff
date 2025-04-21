class BSTIterator(object):
    def __init__(self, root):
        \\\
        :type root: TreeNode
        \\\
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        \\\
        :rtype: int
        \\\
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self):
        \\\
        :rtype: bool
        \\\
        return bool(self.stack)
