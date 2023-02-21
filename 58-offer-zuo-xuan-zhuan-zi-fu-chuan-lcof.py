class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_list = list(s)
        i, j = 0, n - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        i, j = n, len(s) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        i, j = 0, len(s) - 1
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        return "".join(s_list)


print(Solution().reverseLeftWords())
