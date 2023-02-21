import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 0
        q = []
        for n, v in freq.items():
            heapq.heappush(q, (v, n))
            if len(q) > k:
                heapq.heappop(q)
        res = []
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res[::-1]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
