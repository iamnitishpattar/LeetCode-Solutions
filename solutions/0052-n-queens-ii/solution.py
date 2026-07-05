class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(r, cols, pos_diag, neg_diag):
            if r == n: return 1
            res = 0
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag: continue
                res += backtrack(r + 1, cols | {c}, pos_diag | {r + c}, neg_diag | {r - c})
            return res
        return backtrack(0, set(), set(), set())

