from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        res = 0
        while i < len(tokens):
            if tokens[i] in ["+", "-", "*", "/"]:
                n2 = stack.pop(-1)
                n1 = stack.pop(-1)
                op = tokens[i]
                if op == "+":
                    res = n1 + n2
                elif op == "-":
                    res = n1 - n2
                elif op == "*":
                    res = n1 * n2
                elif op == "/":
                    res = int(n1 / n2)
                print(n1, n2, op, res)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack[0]


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
