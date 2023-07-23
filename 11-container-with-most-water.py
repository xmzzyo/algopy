from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_ = 0
        while l < r:
            if height[l] < height[r]:
                max_ = max(max_, height[l] * (r - l))
                l += 1
            else:
                max_ = max(max_, height[r] * (r - l))
                r -= 1
        return max_
