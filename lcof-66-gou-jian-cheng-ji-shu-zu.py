from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [1 for _ in range(len(a))]
        tmp = 1
        for i in range(1, len(a)):
            tmp *= a[i - 1]
            res[i] = tmp
        tmp = 1
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            res[i] *= tmp
        return res
