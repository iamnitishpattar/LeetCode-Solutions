class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, current, total):
            if total == target:
                res.append(current[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])
                current.pop()
        backtrack(0, [], 0)
        return res

