class Solution:
    def integerBreak(self, n: int) -> int:
        arr = [0 for _ in range(59)]
        arr[2] = 1
        for i in range(3, n + 1):
            rest = i - 1
            while rest >= int(i / 2):
                arr[i] = max(arr[i], max((i - rest) * rest, (i - rest) * arr[rest]))
                rest -= 1
        # print(arr)
        return arr[n]


print(Solution().integerBreak(4))
