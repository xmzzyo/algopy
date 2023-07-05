class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        res += 1
                        dp[i][j] = 1
                    else:
                        if dp[i + 1][j - 1]:
                            res += 1
                            dp[i][j] = 1
        return res

    def double_pointer(self, s):
        res = 0

        def expand(l, r):
            e_res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                e_res += 1
            return e_res

        for i in range(len(s)):
            res += expand(i, i)
            res += expand(i, i + 1)
        return res
