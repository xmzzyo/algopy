from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_steps = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, min(len(nums), i + nums[i] + 1)):
                max_steps[j] = min(max_steps[j], max_steps[i] + 1)
        # print(max_steps)
        return max_steps[-1]


print(Solution().jump([2, 3, 0, 1, 4]))
