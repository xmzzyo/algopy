from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        while i < len(pushed):
            if i < len(pushed):
                stack.append(pushed[i])
                i += 1
            while len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop(-1)
                j += 1
        return len(stack) == 0


print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
