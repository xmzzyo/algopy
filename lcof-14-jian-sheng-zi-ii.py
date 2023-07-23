class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 3:
            return 1
        bse = n // 3
        res = n % 3
        ans = 3 ** (bse - 2)
        if res == 0:
            ans *= 3 * 3
        if res == 1:
            ans *= 3 * 4
        if res == 2:
            ans *= 4 * 4
        return ans
