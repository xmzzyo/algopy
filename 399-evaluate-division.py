from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = {}
        for eq, v in zip(equations, values):
            s, t = eq
            if s not in m:
                m[s] = {}
            if t not in m:
                m[t] = {}
            m[s][s] = 1.0
            m[t][t] = 1.0
            m[s][t] = v
            m[t][s] = 1 / v

        print(m)

        def cal(s, t, ans, vis):
            if s not in m or t not in m:
                return -1.
            if s == t:
                return ans * m[s][t]
            for tt, v in m[s].items():
                if (s, tt) in vis:
                    continue
                vis.append((s, tt))
                r = cal(tt, t, ans * v, vis)
                if r:
                    return r

        res = []
        for q in queries:
            r = cal(q[0], q[1], 1, [])
            if not r:
                r = -1
            res.append(r)
        return res


print(Solution().calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                              queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
