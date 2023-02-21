from typing import List
from collections import deque


class MonoQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, val):
        if len(self.queue) > 0 and val == self.queue[0]:
            self.queue.popleft()

    def push(self, x):
        while len(self.queue) > 0 and x > self.queue[-1]:
            self.queue.pop()
        self.queue.append(x)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_queue = MonoQueue()
        res = []
        for n in nums[0: k]:
            mono_queue.push(n)
        res.append(mono_queue.front())
        for end in range(k, len(nums)):
            mono_queue.pop(nums[end - k])
            mono_queue.push(nums[end])
            res.append(mono_queue.front())
        return res


print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
