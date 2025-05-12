class Solution:
    def countSubstrings(self, s: str) -> int:

        def manacher(s):
            t = '^#' + '#'.join(s) + '#$'
            n = len(t)
            pali_radiuses = [0] * n
            left, right = 0, 0
            for i in range(n):
                if i < right:
                    pali_radiuses[i] = min(r - i, pali_radiuses[l + (r - i)])
                else:
                    pali_radiuses[i] = 0
                while (i + pali_radiuses[i] + 1 < n and i - pali_radiuses[i] - 1 >= 0 
                       and t[i + pali_radiuses[i] + 1] == t[i - pali_radiuses[i] - 1]):
                    pali_radiuses[i] += 1
                if i + pali_radiuses[i] > right:
                    l, r = i - pali_radiuses[i], i + pali_radiuses[i]
            return pali_radiuses
        
        p = manacher(s)
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res