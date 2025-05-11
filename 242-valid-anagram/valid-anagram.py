class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1
        key_count = len(char_count.keys())
        for c in t:
            char_count[c] -=1
            if char_count[c] == -1:
                return False
            elif char_count[c] == 0:
                key_count -=1
        return key_count == 0
        