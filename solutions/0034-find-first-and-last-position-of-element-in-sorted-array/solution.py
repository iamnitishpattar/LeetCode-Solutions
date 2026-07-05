import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target) - 1
        if l <= r and l < len(nums) and nums[l] == target:
            return [l, r]
        return [-1, -1]

