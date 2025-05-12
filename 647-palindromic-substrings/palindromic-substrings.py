class Solution:
    def countSubstrings(self, s: str) -> int:

        def manacher(s):
            t = '^#' + '#'.join(s) + '#$'
            n = len(t)
            pali_radiuses = [0] * n
            left, right = 0, 0
            for i in range(n):
                radius = 0
                if i < right:
                    radius = min(right - i, pali_radiuses[left + (right - i)])
                while (i + radius + 1 < n and i - radius - 1 >= 0 
                       and t[i + radius + 1] == t[i - radius - 1]):
                    radius += 1
                if i + radius > right:
                    left, right = i - radius, i + radius
                pali_radiuses[i] = radius
            return pali_radiuses
        
        p = manacher(s)
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res