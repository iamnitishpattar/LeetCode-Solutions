class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right):
            if left > right: return [None]
            res = []
            for val in range(left, right + 1):
                for l in generate(left, val - 1):
                    for r in generate(val + 1, right):
                        res.append(TreeNode(val, l, r))
            return res
        return generate(1, n)

