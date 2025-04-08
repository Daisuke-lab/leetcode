class Solution:
    # Again. start from center
    # Because everytime, you select a different center, it's going to be a different answer
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        for i in range(len(s) -1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
        