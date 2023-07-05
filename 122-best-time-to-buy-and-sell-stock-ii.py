from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                res += diff
        return res

    def dp(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(len(prices))], [0 for _ in range(len(prices))]]
        dp[0][0] = -prices[0]
        dp[1][0] = 0

        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] - prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + prices[i])
        return dp[1][-1]


print(Solution().maxProfit([1, 2, 3, 4, 5]))
