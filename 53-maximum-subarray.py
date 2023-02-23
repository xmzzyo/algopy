import copy
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = copy.deepcopy(nums)
        for i in range(1, len(nums)):
            arr[i] = max(nums[i], arr[i - 1] + nums[i])
        print(arr)
        return max(arr)


print(Solution().maxSubArray([5, 4, -1, 7, 8]))
