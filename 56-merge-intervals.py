from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if len(merged) == 0 or merged[-1][-1] < interval[0]:
                merged.append(interval)
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
