import sys


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(101):
            if i * i > n:
                break
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        return dp[-1]


print(Solution().numSquares(13))
