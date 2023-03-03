from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        flag = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                flag = 0
            dp[0][i] = flag
        flag = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                flag = 0
            dp[i][0] = flag
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


print(Solution().uniquePathsWithObstacles([[1, 0]]))
