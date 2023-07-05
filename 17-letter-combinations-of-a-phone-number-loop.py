import copy

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']}
        res = []
        for d in digits:
            if len(res) == 0:
                res.extend(phone_map[d])
                continue
            cur_len = len(res)
            while cur_len > 0:
                cur_str = res.pop(0)
                for c in phone_map[d]:
                    res.append(cur_str + c)
                cur_len -= 1
        return res

    def slove2(self, digits):
        if len(digits) == 0:
            return []
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']}
        res = []
        path = []

        def backtrack(dn):
            if len(path) == len(digits):
                res.append("".join(copy.deepcopy(path)))
                return

            for i in range(len(dn)):
                for n in phone_map[dn[i]]:
                    path.append(n)
                    backtrack(dn[i+1:])
                    path.pop(-1)

        backtrack(digits)
        return res


print(Solution().slove2("23"))
