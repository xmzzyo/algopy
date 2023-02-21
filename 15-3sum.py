from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            return [nums]
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            cur_sum = set()
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j - 1] and nums[j - 1] == nums[j - 2]:
                    continue
                if -(nums[i] + nums[j]) in cur_sum:
                    cur_sum.remove(-(nums[i] + nums[j]))
                    res.append([nums[i], nums[j], -(nums[i] + nums[j])])
                cur_sum.add(nums[j])
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            return [nums]
        nums.sort()
        res = []
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


print(Solution().threeSum2([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum2([0, 0, 0, 0]))
print(Solution().threeSum2([-2, 0, 0, 2, 2]))
