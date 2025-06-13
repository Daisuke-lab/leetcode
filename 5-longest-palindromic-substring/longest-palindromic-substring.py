class Solution:
    def longestPalindrome(self, s: str) -> str:
        original_s = s
        s = "^#" + "#".join(s) + "#$"
        radiuses = [0 for i in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            radius = 0
            if i < right:
                distance = right - center
                mirror = center - distance
                radius = min(radiuses[mirror], right -i)

            l = i - (radius + 1)
            r = i + (radius + 1)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                radius += 1
            radiuses[i] = radius
            if right < r -1:
                center = i
                right = r -1
        max_radius = max(radiuses)
        max_len = (max_radius * 2) // 2
        center_index = radiuses.index(max_radius)
        # Convert back to original string indices
        start = (center_index - max_len) // 2
        return original_s[start: start + max_len]
             
            
        
