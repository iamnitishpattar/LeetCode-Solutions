class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = p_idx = match = 0
        star_idx = -1
        while s_idx < len(s):
            if p_idx < len(p) and (p[p_idx] == '?' or s[s_idx] == p[p_idx]):
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match = s_idx
                p_idx += 1
            elif star_idx != -1:
                p_idx = star_idx + 1
                match += 1
                s_idx = match
            else:
                return False
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
        return p_idx == len(p)

