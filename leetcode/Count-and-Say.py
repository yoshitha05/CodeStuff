class Solution(object):
    def countAndSay(self, n):
        \\\
        :type n: int
        :rtype: str
        \\\
        if n == 1:
            return \1\
        
        def get_next(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                result.append(str(count) + s[i])
                i += 1
            return \\.join(result)
        
        s = \1\
        for _ in range(n - 1):
            s = get_next(s)
        
        return s