class MinStack(object):

    def __init__(self):
        \\\
        Initialize your data structure here.
        \\\
        self.stack = []
        self.min_stack = []

    def push(self, val):
        \\\
        Push element x onto stack.
        :type val: int
        :rtype: None
        \\\
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        \\\
        Removes the element on top of the stack.
        :rtype: None
        \\\
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        \\\
        Get the top element.
        :rtype: int
        \\\
        return self.stack[-1] if self.stack else None

    def getMin(self):
        \\\
        Retrieve the minimum element in the stack.
        :rtype: int
        \\\
        return self.min_stack[-1] if self.min_stack else None
