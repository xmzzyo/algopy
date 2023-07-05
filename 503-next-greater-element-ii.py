from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums) * 2):
            while len(stack) > 0 and nums[i % len(nums)] > nums[stack[-1]]:
                ans[stack[-1]] = nums[i % len(nums)]
                stack.pop()
            stack.append(i % len(nums))
        return ans
