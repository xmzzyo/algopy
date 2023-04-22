from typing import List


class Solution:
    def cnt(self, str1):
        c0, c1 = 0, 0
        for s in str1:
            if s == '0':
                c0 += 1
            if s == '1':
                c1 += 1
        return c0, c1

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            c0, c1 = self.cnt(s)
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
        return dp[m][n]


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], m=5, n=3))
