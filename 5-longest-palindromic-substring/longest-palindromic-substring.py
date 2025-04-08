class Solution:
    # If you fixing the middle, it can be easy
    # n^2
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = s[l:r+1] if r - l + 1> len(longest) else longest
                l -= 1
                r += 1
        for i in range(len(s) -1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                longest = s[l:r+1] if r - l + 1> len(longest) else longest
                l -= 1
                r += 1
        return longest

                        
