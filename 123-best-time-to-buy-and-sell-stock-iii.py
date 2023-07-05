from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(0 - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] - prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] + prices[i], dp[i - 1][3])
        return dp[-1][3]


print(Solution().maxProfit())
