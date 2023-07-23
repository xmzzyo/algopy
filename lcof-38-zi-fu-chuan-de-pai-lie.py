from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        path = []

        v = [False for _ in range(len(s))]

        def recurse():
            if len(path) == len(s):
                if "".join(path) not in res:
                    res.append("".join(path))
            for i in range(len(s)):
                if v[i]:
                    continue
                v[i] = True
                path.append(s[i])
                recurse()
                path.pop(-1)
                v[i] = False

        recurse()
        return res


print(Solution().permutation("abc"))
