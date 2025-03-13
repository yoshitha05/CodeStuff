class Solution(object):
    def myPow(self, x, n):
        \\\
        :type x: float
        :type n: int
        :rtype: float
        \\\
        if n == 0:
            return 1  # Base case: x^0 = 1
        if n < 0:
            return 1 / self.myPow(x, -n)  # Handle negative exponent

        half = self.myPow(x, n // 2)  # Recursively compute x^(n/2)
        if n % 2 == 0:
            return half * half  # If even: (x^(n/2))^2
        else:
            return x * half * half