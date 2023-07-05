from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(len(prices))]
        for j in range(k):
            dp[0][2 * j + 1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(k):
                dp[i][2 * j + 1] = max(dp[i - 1][2 * j + 1], dp[i - 1][2 * j] - prices[i])
                dp[i][2 * j + 2] = max(dp[i - 1][2 * j + 2], dp[i - 1][2 * j + 1] + prices[i])
        return dp[len(prices) - 1][-1]
