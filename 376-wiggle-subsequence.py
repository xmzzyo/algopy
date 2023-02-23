from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res = 1
        cur_diff = 0
        i = 0
        while i < len(nums) - 1:
            next_diff = nums[i + 1] - nums[i]
            if (next_diff > 0 >= cur_diff) or (next_diff < 0 <= cur_diff):
                res += 1
                cur_diff = next_diff
            i += 1
        return res

    def wiggleMaxLength2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [[], []]
        dp[0] = [1 for _ in range(len(nums))]
        dp[1] = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                if diff > 0:
                    dp[1][i] = max(dp[0][j] + 1, dp[1][i])
                if diff < 0:
                    dp[0][i] = max(dp[1][j] + 1, dp[0][i])
        # print(dp)
        return max(dp[0][len(nums) - 1], dp[1][len(nums) - 1])


print(Solution().wiggleMaxLength2([1, 7, 4, 9, 2, 5]))
