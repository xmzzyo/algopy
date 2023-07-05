import copy

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 1:
            return ["()"]

        def dfs(cur_str, resid_l, resid_r):
            if resid_l == 0 and resid_r == 0:
                res.append(cur_str)
                return
            if resid_r < resid_l:
                return
            if resid_l > 0:
                dfs(cur_str + '(', resid_l - 1, resid_r)
            if resid_r > 0:
                dfs(cur_str + ')', resid_l, resid_r - 1)

        dfs('', n, n)
        return res

    def gen2(self, n):
        if n == 0:
            return []
        res = []
        res.append([None])
        res.append(["()"])
        for i in range(2, n + 1):
            rr = []
            for j in range(i):
                l1 = res[j]
                l2 = res[i - 1 - j]
                for ll1 in l1:
                    for ll2 in l2:
                        if ll1 is None:
                            ll1 = ""
                        if ll2 is None:
                            ll2 = ""
                        e = "(" + ll1 + ")" + ll2
                        rr.append(e)
            res.append(rr)
        return res[-1]


print(Solution().generateParenthesis(3))
