class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        def backtrack(r, cols, pos_diag, neg_diag):
            if r == n: res.append(["".join(row) for row in board]); return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag: continue
                board[r][c] = 'Q'
                backtrack(r + 1, cols | {c}, pos_diag | {r + c}, neg_diag | {r - c})
                board[r][c] = '.'
        backtrack(0, set(), set(), set())
        return res

