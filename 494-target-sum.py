from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        l = s + target
        if l % 2 == 1:
            return 0
        left = int(l / 2)
        dp = [0 for _ in range(left + 1)]
        dp[0] = 1
        for n in nums:
            for t in range(left, n - 1, -1):
                dp[t] += dp[t - n]
        return dp[left]

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        res = []
        path = []
        s = sum(nums)
        if abs(target) > s:
            return 0
        l = s + target
        if l % 2 == 1:
            return 0
        left = int(l / 2)
        nums.sort()

        def backtrack(n_list, t):
            sum_v = 0
            if sum_v == t:
                res.append(path)
                sum_v = 0
            for i in range(len(n_list)):
                sum_v += n_list[i]
                path.append(n_list[i])
                backtrack(n_list[i:], left)
                sum_v -= n_list[i]
                path.pop(n_list[i])

        backtrack(nums, left)
        return len(res)


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
