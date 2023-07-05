from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights.insert(0, 0)
        heights.append(0)
        ans = 0
        for i in range(1, len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, w * h)
            stack.append(i)
        return ans
