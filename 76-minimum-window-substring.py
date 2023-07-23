import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        def match(a, b):
            for k, v in a.items():
                if k not in b or b[k] < v:
                    return False
            return True

        t_map = {}
        for c in t:
            if c not in t_map:
                t_map[c] = 0
            t_map[c] += 1
        print(t_map)
        match_map = {}
        l, r = 0, 0
        min_l = sys.maxsize
        ts, te = 0, 0
        while r <= len(s):
            if match(t_map, match_map):
                print(match_map)
                print(r, l, ts, te, min_l)
                if min_l > r - l:
                    ts, te = l, r
                    min_l = r - l
                if s[l] in match_map:
                    match_map[s[l]] -= 1
                l += 1
            else:
                if r == len(s):
                    break
                print(r, l)
                if s[r] in t_map:
                    if s[r] not in match_map:
                        match_map[s[r]] = 0
                    match_map[s[r]] += 1
                r += 1
        return s[ts:te]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
