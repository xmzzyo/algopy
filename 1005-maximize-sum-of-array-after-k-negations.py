from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k > 0:
            nums[0] = -nums[0]
            nums.sort()
            k -= 1
            if nums[0] > 0:
                if k % 2 == 0:
                    return sum(nums)
                else:
                    return sum(nums[1:]) - nums[0]
        return sum(nums)


print(Solution().largestSumAfterKNegations([5, 6, 9, -3, 3], 2))
