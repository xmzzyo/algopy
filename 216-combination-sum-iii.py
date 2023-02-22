import copy
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(s):
            if len(path) == k:
                if sum(path) == n:
                    res.append(copy.deepcopy(path))
                return

            for i in range(s, 10 - (k - len(path))):
                path.append(i)
                backtrack(i + 1)
                path.pop(-1)

        backtrack(1)
        return res


print(Solution().combinationSum3(3, 7))
