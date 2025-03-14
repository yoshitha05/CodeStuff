class Solution(object):
    def fullJustify(self, words, maxWidth):
        \\\
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        \\\
        res, cur, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            
            cur.append(word)
            num_of_letters += len(word)

        # Left justify the last line
        res.append(' '.join(cur).ljust(maxWidth))
        
        return res