from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS to Build the Parent Graph
        parents = defaultdict(set)
        level = {beginWord}
        found = False
        
        while level and not found:
            next_level = defaultdict(set)
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_level[new_word].add(word)
                            if new_word == endWord:
                                found = True

            wordSet -= set(next_level.keys())  # ✅ FIXED: Convert dictionary keys to set
            level = next_level  # Move to next level
            parents.update(next_level)

        if not found:
            return []

        # Step 2: Backtrack to Construct Paths
        res = []
        
        def backtrack(path, word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for prev in parents[word]:
                backtrack(path + [prev], prev)

        backtrack([endWord], endWord)
        return res
