from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_v = nums[0]
        min_v = nums[0]
        res = max_v
        for i in range(1, len(nums)):
            max_v, min_v = max(max_v * nums[i], min_v * nums[i], nums[i]), min(max_v * nums[i], min_v * nums[i], nums[i])
            res = max(res, max_v)
        return res
