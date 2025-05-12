class Solution:

    def longestPalindrome(self, s: str) -> str:
        # Make "s" to odd length "t"
        # ABBA => #A#B#B#A# can be considerd as palindrome at # as center
        # ^ and $ make sure it doesn't include # as a part of palindroe in algorithm.
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        # max radius of palindrome starting from i
        pali_radiuses = [0] * n
        center = right = 0

        for i in range(2, n - 2):
            radius = 0
            if i < right:
                distance = i - center
                mirror = center - i
                radius = min(right - i, pali_radiuses[mirror])
            l = i - radius - 1
            r = i + radius + 1
            while l >= 0 and r < len(t) and t[l] == t[r]:
                l -= 1
                r += 1
                radius += 1
            pali_radiuses[i] = radius
            if r > right:
                center = i
                right = r
        max_length = max(pali_radiuses)
        index = pali_radiuses.index(max_length)
        start = (index - max_length) // 2
        return s[start:start + max_length]
            

