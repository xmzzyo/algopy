from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > target and nums[i] >= 0:  # prune
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > target and nums[i] >= 0:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                c = target - nums[i] - nums[j]
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > c:
                        r -= 1
                    elif nums[l] + nums[r] < c:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2, 2], 8))
print(Solution().fourSum([-2, -1, -1, 1, 1, 2, 2], 0))
