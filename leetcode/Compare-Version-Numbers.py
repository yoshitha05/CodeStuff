class Solution(object):
    def compareVersion(self, version1, version2):
        \\\
        :type version1: str
        :type version2: str
        :rtype: int
        \\\
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        n = max(len(v1_parts), len(v2_parts))
        
        for i in range(n):
            v1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2 = int(v2_parts[i]) if i < len(v2_parts) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
