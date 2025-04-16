class Solution(object):
    def evalRPN(self, tokens):
        \\\
        :type tokens: List[str]
        :rtype: int
        \\\
        stack = []
        for token in tokens:
            if token not in \+-*/\:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == \+\:
                    stack.append(a + b)
                elif token == \-\:
                    stack.append(a - b)
                elif token == \*\:
                    stack.append(a * b)
                elif token == \/\:
                    stack.append(int(float(a) / b))  # truncate toward zero
        return stack[0]
