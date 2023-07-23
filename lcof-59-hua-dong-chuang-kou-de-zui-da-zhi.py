import collections

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = collections.deque()
        for i in range(len(nums)):
            while len(window) and nums[i] > window[-1][-1]:
                window.pop()
            window.append([i, nums[i]])
            if 0 <= window[0][0] < i - k + 1:
                window.popleft()
            if i >= k - 1:
                res.append(window[0][-1])
        return res


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().maxSlidingWindow([1, -1], 1))
