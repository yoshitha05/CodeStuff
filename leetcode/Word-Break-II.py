class Solution(object):
    def wordBreak(self, s, wordDict):
        \\\
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        \\\
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [\\]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in backtrack(end):
                        res.append(word + (\\ if sub == \\ else \ \) + sub)

            memo[start] = res
            return res

        return backtrack(0)
