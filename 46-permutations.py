import copy

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        n = len(nums)

        def recur():
            if len(path) == n:
                ans.append(copy.deepcopy(path))

            for j in range(n):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                recur()
                path.pop(-1)

        recur()
        return ans
