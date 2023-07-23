from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0
        for i in nums:
            if i == 0:
                c0 += 1
            if i == 1:
                c1 += 1
            if i == 2:
                c2 += 1
        idx = 0
        while c0 > 0:
            nums[idx] = 0
            idx += 1
            c0 -= 1
        while c1 > 0:
            nums[idx] = 1
            idx += 1
            c1 -= 1
        while c2 > 0:
            nums[idx] = 2
            idx += 1
            c2 -= 1
