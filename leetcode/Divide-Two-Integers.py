class Solution(object):
    def divide(self, dividend, divisor):
        \\\
        :type dividend: int
        :type divisor: int
        :rtype: int
        \\\
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamped to 32-bit signed integer range

        # Get sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1  

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Double until just below dividend
                temp <<= 1
                multiple <<= 1

            dividend -= temp  # Subtract the biggest chunk possible
            quotient += multiple  # Add corresponding multiple to quotient
 
        return sign * quotient 
