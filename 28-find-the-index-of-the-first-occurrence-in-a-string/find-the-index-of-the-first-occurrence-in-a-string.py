class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.create_lps(needle)

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

            if j == len(needle):
                return i - j
        return -1


    def create_lps(self, word):
        lps = [0] * len(word)
        prev_lps, i = 0, 1
        while i < len(word):
            if word[i] == word[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps-1]
        return lps
        