from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(v):
            l, r = 0, len(v) - 1
            while l <= r:
                mid = l + int((r - l) / 2)
                if v[mid] > target:
                    r = mid - 1
                if v[mid] < target:
                    l = mid + 1
                if v[mid] == target:
                    return True
            return False

        for i in range(len(matrix)):
            if find_row(matrix[i]):
                return True
        return False


m = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(Solution().findNumberIn2DArray(m, 19))
