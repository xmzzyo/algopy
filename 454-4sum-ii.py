from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1 = {}
        for i in nums1:
            for j in nums2:
                val = i + j
                if val in dict1:
                    dict1[val] += 1
                else:
                    dict1[val] = 1
        res = 0
        for i in nums3:
            for j in nums4:
                val = -(i + j)
                if val in dict1:
                    res += dict1[val]
        return res


print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
print(Solution().fourSumCount([0], [0], [0], [0]))
