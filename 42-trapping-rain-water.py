from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        s = 0
        for i in range(1, len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top_h = height[stack.pop()]
                if len(stack) > 0:
                    h = min(height[stack[-1]], height[i]) - top_h
                    w = i - stack[-1] - 1
                    s += h * w
            stack.append(i)
        return s

    def trap_v2(self, height: List[int]) -> int:
        max_l, max_r = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        max_l[0] = height[0]
        for i in range(1, len(height)):
            max_l[i] = max(max_l[i - 1], height[i])
        max_r[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i])
        s = 0
        for i in range(len(height)):
            h = min(max_l[i], max_r[i]) - height[i]
            if h > 0:
                s += h
        return s
