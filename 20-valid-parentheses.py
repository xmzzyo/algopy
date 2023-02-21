class Solution:

    def check_pair(self, c1, c2):
        # print(c1, c2)
        if c1 == "(" and c2 == ")":
            return True
        if c1 == "[" and c2 == "]":
            return True
        if c1 == "{" and c2 == "}":
            return True
        return False

    def isValid(self, s: str) -> bool:
        q = []
        for c in s:
            if c in ["(", "[", "{"]:
                q.append(c)
            else:
                if len(q) == 0 or not self.check_pair(q.pop(-1), c):
                    return False
        if len(q) > 0:
            return False
        return True


print(Solution().isValid("()[]{}"))
