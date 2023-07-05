from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]
        res = 0
        for i in range(1, len(nums2) + 1):
            for j in range(1, len(nums1) + 1):
                if nums2[i - 1] == nums1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4]))
