class Solution(object):
    def multiply(self, num1, num2):
        \\\
        :type num1: str
        :type num2: str
        :rtype: str
        \\\
        if num1 == \0\ or num2 == \0\:
            return \0\

        m, n = len(num1), len(num2)
        res = [0] * (m + n)  # Array to store results

        # Reverse iteration for multiplication
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + res[i + j + 1]  # Add to previous stored value

                res[i + j + 1] = sum_ % 10   # Store last digit
                res[i + j] += sum_ // 10     # Carry forward

        # Convert result array to string, removing leading zeros
        result = \\.join(map(str, res)).lstrip(\0\)
        return result if result else \0\