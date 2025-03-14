class Solution(object):
    def isNumber(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        pattern = r'^[+-]?(\\d+(\\.\\d*)?|\\.\\d+)([eE][+-]?\\d+)?$'
        return bool(re.match(pattern, s.strip()))