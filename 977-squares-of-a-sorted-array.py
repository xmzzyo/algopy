from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        neg_idx = len(nums) - 1
        while neg_idx >= 0 and nums[neg_idx] > 0:
            neg_idx -= 1
        l, r = neg_idx, neg_idx + 1
        for i in range(len(nums)):
            nums[i] *= nums[i]
        while l >= 0 and r < len(nums):
            while l >= 0 and nums[l] <= nums[r]:
                res.append(nums[l])
                l -= 1
            while r < len(nums) and nums[l] > nums[r]:
                res.append(nums[r])
                r += 1
        while l >= 0:
            res.append(nums[l])
            l -= 1
        while r < len(nums):
            res.append(nums[r])
            r += 1
        return res


if __name__ == "__main__":
    # print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
    # print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
    # print(Solution().sortedSquares([-5,-3,-2,-1]))
    # print(Solution().sortedSquares([1, 3, 5, 7]))
    # print(Solution().sortedSquares([-2, 0]))
    print(Solution().sortedSquares([-3, 0, 2]))
