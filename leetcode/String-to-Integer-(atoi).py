class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0

        sign = 1
        index = 0
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            index += 1

        result = 0
        while index < len(s) and s[index].isdigit(): 
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        # Clamp result to 32-bit integer range
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result 
