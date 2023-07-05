from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums2))]
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                ans[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        print(ans)
        res = []
        for n in nums1:
            for i in range(len(nums2)):
                if n == nums2[i]:
                    res.append(ans[i])
                    break
        return res


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
print(Solution().nextGreaterElement([1, 3, 5, 2, 4], [5, 4, 3, 2, 1]))
