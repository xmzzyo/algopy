from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  # wrong answer
        def helper(l, r):
            if l == r:
                return -1, -1
            l1, l2, r1, r2 = -1, -1, -1, -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    if target != nums[m - 1] and target != nums[m + 1]:
                        return m, m
                    if nums[m - 1] == target:
                        l1, r1 = helper(l, m - 1)
                    if nums[m + 1] == target:
                        l2, r2 = helper(m + 1, r)
                    return max(l1, l2), max(r1, r2)

        return helper(0, len(nums) - 1)


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
