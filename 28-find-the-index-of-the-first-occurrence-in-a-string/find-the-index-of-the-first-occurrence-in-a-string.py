class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.create_lps(needle)

        i, j = 0, 0
        while i < len(haystack):
            # when chars match
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # don't start from j=0, we can utilize lps
            elif j != 0:
                j = lps[j-1]
            # when j=0, nothing can match with i, so move on
            else:
                i += 1
                

            if j == len(needle):
                return i - j
        return -1


    def create_lps(self, word):
        lps = [0] * len(word)
        prev_lps, i = 0, 1
        while i < len(word):
            # when you can utilize the previous suffix/prefix
            if word[i] == word[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            # if the first condition doesn't work, you go back and search suffix/prefix you can use
            elif prev_lps != 0:
                prev_lps = lps[prev_lps-1]
            # when there is not suffix/prefix you can use
            else:
                lps[i] = 0
                i += 1
                
        return lps
        