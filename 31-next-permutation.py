from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        r = len(nums) - 1
        pre = nums[-1]
        while r > 0:
            if pre > nums[r]:
                reverse()
            else:
                pre = nums[r]
                r -= 1
        if r == 0:
