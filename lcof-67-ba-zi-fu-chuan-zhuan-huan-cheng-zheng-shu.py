class Solution:
    def strToInt(self, str: str) -> int:
        res = []
        i = 0
        flag = False
        while i < len(str):
            if str[i] not in ["-", "+"] + [f"{k}" for k in range(10)]:
                if flag:
                    break
            else:
                flag = True
                res.append(str[i])
