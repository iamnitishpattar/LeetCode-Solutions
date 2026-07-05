import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums, res = list(range(1, n + 1)), []
        k -= 1
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res.append(str(nums.pop(idx)))
        return "".join(res)

