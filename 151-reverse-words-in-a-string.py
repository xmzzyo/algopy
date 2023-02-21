class Solution:
    def reverseWords(self, s: str) -> str:
        def trim_head_tail_space(ss: str):
            p = 0
            while p < len(ss) and ss[p] == " ":
                p += 1
            return ss[p:]

        # Trim the head and tail space
        s = trim_head_tail_space(s)
        s = trim_head_tail_space(s[::-1])[::-1]

        pf, ps, s = 0, 0, s[::-1]  # Reverse the string.
        while pf < len(s):
            if s[pf] == " ":
                # Will not excede. Because we have clean the tail space.
                if s[pf] == s[pf + 1]:
                    s = s[:pf] + s[pf + 1:]
                    continue
                else:
                    s = s[:ps] + s[ps: pf][::-1] + s[pf:]
                    ps, pf = pf + 1, pf + 2
            else:
                pf += 1
        # Must do the last step, because the last word is omit though the pointers are on the correct positions,
        return s[:ps] + s[ps:][::-1]


print(Solution().reverseWords("a good   example"))
