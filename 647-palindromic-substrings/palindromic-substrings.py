class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '^#' + '#'.join(s) + '#$'
        n = len(t)
        pali_radiuses = [0] * n
        center, right = 0, 0
        count = 0
        for i in range(2, n-2):
            radius = 0
            if i < right:
                distance = i - center
                mirror = center - distance
                radius = min(right - i, pali_radiuses[mirror])
            l = i - radius - 1
            r = i + radius + 1
            while l >= 0 and r < n and t[l] == t[r]:
                l -= 1
                r += 1
                radius += 1
            if r > right:
                center, right = i, r - 1
            pali_radiuses[i] = radius
            count += (radius + 1) // 2
        return count
