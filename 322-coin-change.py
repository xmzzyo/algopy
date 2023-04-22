from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                if dp[j - coins[i]] != 100000:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        if dp[-1] == 100000:
            return -1
        else:
            return dp[-1]


print(Solution().coinChange([1, 2, 5], 11))
