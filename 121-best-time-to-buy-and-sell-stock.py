import sys

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_s = sys.maxsize
        max_p = 0
        for i in range(len(prices)):
            min_s = min(min_s, prices[i])
            max_p = max(max_p, prices[i] - min_s)
        return max_p


print(Solution().maxProfit())
