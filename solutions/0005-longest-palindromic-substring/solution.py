class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # (right - left - 1) is the length of the palindrome found
            if right - left - 1 > max_len:
                max_len = right - left - 1
                start = left + 1

        for i in range(len(s)):
            expand(i, i)      # odd-length palindromes  (e.g. "aba")
            expand(i, i + 1)  # even-length palindromes (e.g. "abba")

        return s[start:start + max_len]

