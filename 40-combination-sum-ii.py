import copy
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        print(sum(candidates))
        if sum(candidates) < target:
            return res
        path = []
        candidates.sort()

        def backtrack(s):
            if sum(path) == target:
                if path not in res:
                    res.append(copy.deepcopy(path))

            for i in range(s, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1)
                path.pop(-1)

        backtrack(0)

        return res


print(Solution().combinationSum2(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 30))
