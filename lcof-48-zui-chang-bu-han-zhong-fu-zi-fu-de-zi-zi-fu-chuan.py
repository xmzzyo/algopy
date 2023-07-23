class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_l = 1
        l, r = 0, 0
        while r < len(s):
            if r > l and s[r] in s[l:r]:
                if r - l + 1 > max_l:
                    max_l = r - l
                idx = s[l:r].index(s[r]) + l
                l = idx + 1
            r += 1
        return max(max_l, r-l)