class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "^#" + "#".join(s) + "#$"
        radiuses = [0 for i in range(len(t))]
        center = 0
        right = 0
        for i in range(len(t)):
            radius = 0
            if i < right:
                distance = right - center
                mirror = center - distance

            l = i - (radius + 1)
            r = i + (radius + 1)
            while l > 0 and r < len(t) and t[l] == t[r]:
                l -= 1
                r += 1
                radius += 1
            radiuses[i] = radius
            if r -1> right:
                center = i
                right = r -1
        max_radius = max(radiuses)
        center_index = radiuses.index(max_radius)
        start = (center_index - max_radius) // 2
        end = (center_index + max_radius) // 2
        return s[start:end]