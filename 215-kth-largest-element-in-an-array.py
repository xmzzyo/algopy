from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(data, i, j):
            if i > j:
                return data[i]
            left, right = i, j
            pivot = data[left]
            while left < right:
                while left < right and data[right] >= pivot:
                    right -= 1
                data[left] = data[right]
                while left < right and data[left] <= pivot:
                    left += 1
                data[right] = data[left]
            data[left] = pivot
            if left == len(data) - k:
                return data[left]
            if left > len(data) - k:
                return quicksort(data, i, left - 1)
            else:
                return quicksort(data, left + 1, j)

        res = quicksort(nums, 0, len(nums) - 1)
        return res


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
