import copy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(si):
            if path not in res:
                res.append(copy.deepcopy(path))
            for i in range(si, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop(-1)

        backtrack(0)
        return res


print(Solution().subsets([0]))
