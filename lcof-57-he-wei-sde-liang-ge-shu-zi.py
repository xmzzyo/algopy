from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = set()
        for n in nums:
            if target - n in t:
                return [n, target - n]
            t.add(n)
        return []
