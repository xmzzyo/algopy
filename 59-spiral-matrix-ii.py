from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0 for _ in range(n)])
        si, sj = 0, 0
        cur_n = n
        s = 1
        while cur_n >= 1:
            for kj in range(sj, sj + cur_n):
                matrix[si][kj] = s
                s += 1
            for ki in range(si + 1, si + cur_n):
                matrix[ki][sj + cur_n - 1] = s
                s += 1
            for kj in range(sj + cur_n - 2, sj - 1, -1):
                matrix[si + cur_n - 1][kj] = s
                s += 1
            for ki in range(si + cur_n - 2, si, -1):
                matrix[ki][sj] = s
                s += 1
            si, sj = si + 1, sj + 1
            cur_n -= 2
        return matrix


if __name__ == "__main__":
    print(Solution().generateMatrix(4))
