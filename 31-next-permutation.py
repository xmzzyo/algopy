from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        print(i)
        if i == 0:
            nums.sort()
            # print(nums)
            return
        for j in range(len(nums) - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                print(j)
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                print(nums)
                break
        r = len(nums) - 1
        while i < r:
            nums[i], nums[r] = nums[r], nums[i]
            i += 1
            r -= 1
        print(nums)


Solution().nextPermutation([1, 3, 2])
# Solution().nextPermutation([1, 2, 3])
# Solution().nextPermutation([3, 2, 1])
# Solution().nextPermutation([1, 1, 5])
