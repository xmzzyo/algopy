import copy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(s):
            if len(path) == k:
                res.append(copy.deepcopy(path))
                return
            for sn in range(s, n + 1):
                path.append(sn)
                backtrack(sn + 1)
                path.pop(-1)

        backtrack(1)

        return res


print(Solution().combine(4, 2))
