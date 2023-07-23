import heapq

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mx, mi = [], []
        for idx, i in enumerate(nums1 + nums2):
            if idx == 0:
                heapq.heappush(mx, -i)
            else:
                if i > -mx[0]:
                    heapq.heappush(mi, i)
                else:
                    heapq.heappush(mx, -i)
        while abs(len(mi) - len(mx)) > 1:
            if len(mi) > len(mx):
                heapq.heappush(mx, -heapq.heappop(mi))
            if len(mx) > len(mi):
                heapq.heappush(mi, -heapq.heappop(mx))
        if len(mi) > len(mx):
            return mi[0]
        if len(mi) < len(mx):
            return -mx[0]
        else:
            return (mi[0] - mx[0]) / 2
