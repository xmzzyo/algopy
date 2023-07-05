from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
