class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1
        for k, v in s_dict.items():
            if k not in t_dict or t_dict[k] != v:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isAnagram("rat", "cat"))
