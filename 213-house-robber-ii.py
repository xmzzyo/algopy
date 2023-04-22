from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def rob_list(nl):
            if len(nl) == 1:
                return nl[0]
            dp = [0 for _ in range(len(nl))]
            dp[0] = nl[0]
            dp[1] = max(nl[0], nl[1])
            for i in range(2, len(nl)):
                dp[i] = max(dp[i - 2] + nl[i], dp[i - 1])
            return dp[-1]
        return max(rob_list(nums[1:]), rob_list(nums[:-1]))


print(Solution().rob([2, 3, 2]))
print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([1, 2, 3]))
