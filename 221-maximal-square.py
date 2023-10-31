from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        tmp = [int(e) for e in matrix[0]]
        max_s = max(tmp)
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    tmp[j] = 0
                else:
                    tmp[j] += 1
            for j in range(len(matrix[0])):
                if tmp[j] == 0:
                    continue
                elif (j + tmp[j]) <= len(matrix[0]):
                    flag = True
                    for k in range(j + 1, j + tmp[j]):
                        if tmp[k] < tmp[j]:
                            flag = False
                            break
                    if flag:
                        max_s = max(max_s, tmp[j] ** 2)
            print(i, max_s, tmp)
        return max_s

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_s = 0
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            max_s = max(max_s, dp[i][0])
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            max_s = max(max_s, dp[0][j])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j]):
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    max_s = max(max_s, dp[i][j])
        return max_s ** 2


# print(Solution().maximalSquare(
#     [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
# print(Solution().maximalSquare([["0", "1"], ["1", "0"]]))
# print(Solution().maximalSquare([["1", "1"], ["1", "1"]]))
print(
    Solution().maximalSquare2([["1", "0", "1", "0"], ["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]]))
