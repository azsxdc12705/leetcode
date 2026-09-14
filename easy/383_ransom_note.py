class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for i in magazine:
            cnt[ord(i) - ord('a')] += 1
        for i in ransomNote:
            if cnt[ord(i) - ord('a')] > 0:
                cnt[ord(i) - ord('a')] -= 1
            else:
                return False
        return True