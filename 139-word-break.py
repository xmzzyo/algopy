from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(len(s) + 1):
            for j in range(len(wordDict)):
                if i < len(wordDict[j]):
                    continue
                # print(s[i - len(wordDict[j]): i], wordDict[j], dp[i - len(wordDict[j])])
                if s[i - len(wordDict[j]): i] == wordDict[j] and dp[i - len(wordDict[j])] == 1:
                    dp[i] = 1
        return dp[-1] == 1


print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
