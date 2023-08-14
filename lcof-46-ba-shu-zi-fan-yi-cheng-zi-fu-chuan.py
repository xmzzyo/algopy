class Solution:
    def translateNum(self, num: int) -> int:
        dp = [0 for _ in range(len(str(num)) + 1)]
        dp[0] = 1
        dp[1] = 1
        str_num = str(num)
        for i in range(1, len(str_num)):
            if int(str_num[i - 1]) == 1 or (int(str_num[i - 1]) == 2 and int(str_num[i]) < 6):
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]
        return dp[-1]


print(Solution().translateNum(12258))
