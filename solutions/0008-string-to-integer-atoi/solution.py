class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        s = s.lstrip()  # Step 1: strip leading whitespace

        if not s:
            return 0

        sign = 1
        i = 0

        # Step 2: check sign
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        # Step 3: read digits
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Step 4: clamp to 32-bit range
        return max(INT_MIN, min(INT_MAX, result))

