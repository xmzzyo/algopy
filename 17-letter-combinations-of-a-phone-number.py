import copy
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        path = []
        maps = {"2": ['a', 'b', 'c'],
                "3": ['d', 'e', 'f'],
                "4": ['g', 'h', 'i'],
                "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'],
                "7": ['p', 'q', 'r', 's'],
                "8": ['t', 'u', 'v'],
                "9": ['w', 'x', 'y', 'z']}

        def backtrack(s):
            if len(path) == len(digits):
                res.append(copy.deepcopy("".join(path)))
                return

            for i in range(len(s)):
                for j in maps[s[i]]:
                    path.append(j)
                    backtrack(s[i + 1:])
                    path.pop(-1)

        backtrack(digits)
        return res


print(Solution().letterCombinations("23"))
