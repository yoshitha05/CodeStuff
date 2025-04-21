class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        \\\
        :type numerator: int
        :type denominator: int
        :rtype: str
        \\\
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        res.append('.')
        
        remainder = numerator % denominator
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                res.insert(remainder_map[remainder], '(')
                res.append(')')
                break
            remainder_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        
        return ''.join(res)
