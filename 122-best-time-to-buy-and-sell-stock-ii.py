from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                res += diff
        return res


print(Solution().maxProfit([1, 2, 3, 4, 5]))
