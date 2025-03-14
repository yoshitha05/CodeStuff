class Solution(object):
    def getPermutation(self, n, k):
        \\\
        :type n: int
        :type k: int
        :rtype: str
        \\\
        numbers = list(range(1, n + 1))  # List of numbers to pick from
        k -= 1  # Convert k to zero-based index
        result = []
        
        # Compute factorial values
        fact = math.factorial(n - 1)
        
        for i in range(n - 1, -1, -1):
            index = k // fact  # Determine the index of the current digit
            result.append(str(numbers[index]))  # Pick the digit
            numbers.pop(index)  # Remove from list
            if i > 0:
                k %= fact  # Update k for next iteration
                fact //= i  # Update factorial for next level
        
        return \\.join(result)