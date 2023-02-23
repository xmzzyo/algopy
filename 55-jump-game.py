from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_len = 0
        i = 0
        while i <= max_len:
            max_len = max(max_len, nums[i] + i)
            if max_len >= len(nums) - 1:
                return True
            i += 1
        return False


print(Solution().canJump([2, 0, 0]))
