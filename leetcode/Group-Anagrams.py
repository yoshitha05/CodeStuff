class Solution(object):
    def groupAnagrams(self, strs):
        \\\
        :type strs: List[str]
        :rtype: List[List[str]]
        \\\
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_key = \\.join(sorted(word))  # Sort the word to form key
            anagram_map[sorted_key].append(word)  # Append original word

        return list(anagram_map.values())