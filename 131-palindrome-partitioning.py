import copy
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(si):
            if si >= len(s):
                res.append(copy.deepcopy(path))
                return
            for i in range(si, len(s)):
                subs = s[si:i + 1]
                is_palindrome = subs == subs[::-1]
                if is_palindrome:
                    path.append(subs)
                else:
                    continue
                backtrack(i + 1)
                path.pop(-1)

        backtrack(0)
        return res


print(Solution().partition("aab"))
