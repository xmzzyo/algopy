class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        i, j = 0, k - 1
        while j < len(s):
            tmp_i, tmp_j = i, j
            while tmp_i < tmp_j:
                s_list[tmp_i], s_list[tmp_j] = s_list[tmp_j], s_list[tmp_i]
                tmp_i += 1
                tmp_j -= 1
            i += 2 * k
            j = i + k - 1
        j = len(s) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return "".join(s_list)


print(Solution().reverseStr("abcdefgh", k=3))
