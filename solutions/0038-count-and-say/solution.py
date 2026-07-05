class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            next_s = []
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    next_s.append(str(count) + s[i - 1])
                    count = 1
            next_s.append(str(count) + s[-1])
            s = "".join(next_s)
        return s

