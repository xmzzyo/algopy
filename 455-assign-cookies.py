from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i, j = len(g) - 1, len(s) - 1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                res += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return res


print(Solution().findContentChildren([1, 2], [1, 2, 3]))
