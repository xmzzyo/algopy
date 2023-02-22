import copy
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def valid_ip(ss):
            if ss[0] == '0' and len(ss) > 1:
                return False
            for sss in ss:
                if sss > '9' or sss < '0':
                    return False
            if int(ss) > 255:
                return False
            return True

        def backtrack(si):
            if si >= len(s) and len(path) == 4:
                res.append(copy.deepcopy(path))
                return

            for i in range(si, len(s)):
                if valid_ip(s[si:i + 1]):
                    path.append(s[si:i + 1])
                else:
                    continue
                backtrack(i + 1)
                path.pop(-1)

        backtrack(0)
        return [".".join(p) for p in res]


print(Solution().restoreIpAddresses("25525511135"))
