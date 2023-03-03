class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1 for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]


print(Solution().uniquePaths(3, 2))
