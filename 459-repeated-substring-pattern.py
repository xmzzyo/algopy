class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        next_array = [0 for _ in range(len(s))]
        l = 0
        for i in range(1, len(s)):
            while l > 0 and s[i] != s[l]:
                l = next_array[l - 1]
            if s[i] == s[l]:
                l += 1
            next_array[i] = l
        if next_array[-1] != 0 and len(s) % (len(s) - next_array[-1]) == 0:
            return True
        else:
            return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        repeat_len = 1
        while repeat_len <= int(len(s) / 2):
            flag = True
            for i in range(repeat_len, len(s)):
                if s[i] != s[i % repeat_len]:
                    flag = False
                    break
            if flag:
                return True
            else:
                repeat_len += 1
                while len(s) % repeat_len != 0:
                    repeat_len += 1
        return False


print(Solution().repeatedSubstringPattern2("abaababaab"))
