class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        \\\
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        \\\
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookup
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, no valid sequence

        queue = deque([(beginWord, 1)])  # (current_word, level)
        
        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length  # Return shortest transformation length
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    
                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        wordSet.remove(newWord)  # Remove visited word from the set

        return 0  # If no path is found