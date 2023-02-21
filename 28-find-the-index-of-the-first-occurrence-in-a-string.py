class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        next_arr = [0 for _ in range(len(needle))]
        for i in range(1, len(needle)):
            while l > 0 and needle[i] != needle[l]:
                l = next_arr[l - 1]
            if needle[i] == needle[l]:
                l += 1
            next_arr[i] = l
        # print(next_arr)
        i, j = 0, 0
        while i < len(haystack):
            while j > 0 and needle[j] != haystack[i]:
                j = next_arr[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            i += 1
            if j == len(needle):
                return i - len(needle)
        return -1


print(Solution().strStr("leetcode", "leeto"))
