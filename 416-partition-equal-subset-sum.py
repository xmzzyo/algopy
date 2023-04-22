from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = int(sum(nums) / 2)
        dp = [0 for _ in range(target + 1)]
        for n in nums:
            if n > target:
                return False
            for t in range(target, n - 1, -1):
                dp[t] = max(dp[t], dp[t - n] + n)
        return dp[target] == target


print(Solution().canPartition([2, 2, 3, 5]))
