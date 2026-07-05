class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_letters = [], [], 0
        for w in words:
            if num_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_letters = [], 0
            cur.append(w)
            num_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

