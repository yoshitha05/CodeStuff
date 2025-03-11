class Solution(object):
    def findSubstring(self, s, words):
        \\\
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        \\\
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):  # Check all possible starting points
            left, right = i, i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1

                    while current_count[word] > word_count[word]:  # Remove extra words
                        current_count[s[left:left + word_len]] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)
                
                else:
                    current_count.clear()
                    left = right

        return result