class Solution:
    def countSubstrings(self, s: str) -> int:

        def manacher(s):
            t = '^#' + '#'.join(s) + '#$'
            n = len(t)
            pali_radiuses = [0] * n
            l, r = 0, 0
            for i in range(n):
                pali_radiuses[i] = min(r - i, pali_radiuses[l + (r - i)]) if i < r else 0
                while (i + pali_radiuses[i] + 1 < n and i - pali_radiuses[i] - 1 >= 0 
                       and t[i + pali_radiuses[i] + 1] == t[i - pali_radiuses[i] - 1]):
                    pali_radiuses[i] += 1
                if i + pali_radiuses[i] > r:
                    l, r = i - pali_radiuses[i], i + pali_radiuses[i]
            return pali_radiuses
        
        p = manacher(s)
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res