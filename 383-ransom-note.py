class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = [0 for _ in range(26)]
        for c in magazine:
            magazine_dict[ord(c) - ord('a')] += 1
        for c in ransomNote:
            magazine_dict[ord(c) - ord('a')] -= 1
            if magazine_dict[ord(c) - ord('a')] < 0:
                return False
        return True


print(Solution().canConstruct("aa", "aab"))
