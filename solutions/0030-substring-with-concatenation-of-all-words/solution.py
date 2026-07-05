from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = Counter(words)
        res = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(i, i + total_len, word_len):
                w = s[j:j+word_len]
                if w in word_count:
                    seen[w] = seen.get(w, 0) + 1
                    if seen[w] > word_count[w]:
                        break
                else:
                    break
            else:
                res.append(i)
        return res

