from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        主要是看每一个元素被操作的次数，每个元素在滑动窗后进来操作一次，出去操作一次，每个元素都是被操作两次，所以时间复杂度是 2 × n 也就是O(n)。
        :param target:
        :param nums:
        :return:
        """
        lens = len(nums) + 1
        i, j = 0, 0
        cur_sum = nums[0]
        while i < len(nums) and j < len(nums):
            while j < len(nums):
                if cur_sum >= target:
                    lens = min(lens, j - i + 1)
                    cur_sum -= nums[i]
                    i += 1
                    break
                j += 1
                if j >= len(nums):
                    break
                cur_sum += nums[j]
        return lens if lens <= len(nums) else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(Solution().minSubArrayLen(4, [1, 4, 4]))
    print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
