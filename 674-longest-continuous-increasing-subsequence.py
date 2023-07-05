from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))
print(Solution().findLengthOfLCIS([2, 2, 2, 2, 2]))
