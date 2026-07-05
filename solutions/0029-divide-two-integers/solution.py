class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                res += 1 << i
                dividend -= divisor << i
        res *= sign
        return max(-2**31, min(res, 2**31 - 1))

