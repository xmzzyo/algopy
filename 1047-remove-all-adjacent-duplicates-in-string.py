class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop(-1)
                continue
            else:
                stack.append(c)
        return "".join(stack)


print(Solution().removeDuplicates("abbaca"))
