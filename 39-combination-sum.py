from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack():
            if sum(path) > target:
                return
            if sum(path) == target:
                new_p = sorted(path)
                if new_p not in res:
                    res.append(new_p)
                return

            for e in candidates:
                path.append(e)
                backtrack()
                path.pop(-1)

        backtrack()
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
