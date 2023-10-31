from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s, e = -1, - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                if mid==0 or nums[mid] != nums[mid - 1]:
                    s = mid
                    break
                else:
                    r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                if mid== len(nums)-1 or nums[mid] != nums[mid + 1]:
                    e = mid
                    break
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [s, e]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
