from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a, b, = 0, len(nums) - 1
        while a <= b:
            while nums[b] == val:
                b -= 1
                if b == -1:
                    return 0
                if b < a:
                    return a
            if nums[a] == val:
                nums[a], nums[b] = nums[b], nums[a]
                b -= 1
            a += 1
        return a

    def removeElement1(self, nums: List[int], val: int) -> int:
        slow_idx, fast_idx = 0, 0
        while fast_idx < len(nums):
            if nums[fast_idx] != val:
                slow_idx += 1
                nums[slow_idx] = nums[fast_idx]  # overlap, can change array elements
                fast_idx += 1
        return slow_idx

    def removeElement2(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            while nums[l] != val and l <= r:
                l += 1
            while nums[r] == val and l <= r:
                r -= 1
            if l < r:
                l += 1
                r -= 1
                nums[l] = nums[r]
        return l


if __name__ == "__main__":
    print(Solution().removeElement2([2, 2, 3], 2))
