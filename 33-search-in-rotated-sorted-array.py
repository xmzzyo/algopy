from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + int((r - l) / 2)
            if target == nums[m]:
                return m
            if target >= nums[0]:
                if target < nums[m] or nums[m] < nums[0]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] or nums[m] >= nums[0]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([1], 0))
