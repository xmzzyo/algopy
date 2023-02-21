from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = left + int((left - right) / 2)
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
