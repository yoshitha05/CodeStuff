class Solution(object):
    def restoreIpAddresses(self, s):
        \\\
        :type s: str
        :rtype: List[str]
        \\\
        res = []
        
        def backtrack(start, path):
            # If we have 4 segments and used all characters, it's a valid IP
            if len(path) == 4 and start == len(s):
                res.append(\.\.join(path))
                return
            
            # If we already have 4 segments but still have characters left, stop
            if len(path) == 4 and start < len(s):
                return
            
            # Try every possible segment length (1 to 3)
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start:start + length]
                
                # Check if the segment is valid
                if (segment[0] == \0\ and len(segment) > 1) or int(segment) > 255:
                    continue
                
                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res