class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        for i in range(len(s)):
            if stack and s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                max_len = max(max_len, i - (stack[-1] if stack else -1))
            else:
                stack.append(i)

        return max_len


print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses(")()())"))
print(Solution().longestValidParentheses(""))
