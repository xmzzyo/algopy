class Solution:
    def replaceSpace(self, s: str) -> str:
        cnt = 0
        for c in s:
            if c == " ":
                cnt += 1
        if cnt == 0:
            return s
        i = len(s) - 1
        s += " " * cnt * 2
        s_list = list(s)
        j = len(s) - 1
        while i >= 0:
            if s_list[i] != " ":
                s_list[j] = s_list[i]
                j -= 1
                i -= 1
            else:
                s_list[j - 2], s_list[j - 1], s_list[j] = "%", "2", "0"
                j -= 3
                i -= 1
        return "".join(s_list)


print(Solution().replaceSpace("     "))
