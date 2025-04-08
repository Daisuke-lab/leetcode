class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        s_set = set(s)
        t_set = set(t)
        if len(s_set) == 1 and len(t_set) == 1:
            if list(s_set)[0] == list(t_set)[0]:
                return len(s) + len(t)

                
        longest = 1
        for m in range(len(s)):
            longest = max(self.get_longest_s(s, t, m, m), longest)
            longest = max(self.get_longest_s(s, t, m, m+1), longest)
        for m in range(len(t)):
            longest = max(self.get_longest_t(s, t, m, m), longest)
            longest = max(self.get_longest_t(s, t, m, m+1), longest)
        return longest
            

    def get_longest_t(self, s, t, l, r):
        length = 0
        while l >= 0 and r < len(t) and t[l] == t[r]:
            length = r - l + 1
            l -=1
            r += 1
        if r == len(t) or t[r] not in s:
            return length
        
        # you still have possibility to extend with t
        ls = [i for i in range(len(s)) if s[i] == t[r]]
        saved_r = r
        longest = length
        saved_length = length
        for l in ls:
            r = saved_r
            length = saved_length
            while l >= 0 and r < len(t) and s[l] == t[r]:
                length += 2
                l -=1
                r += 1
            longest = max(longest, length)
        return longest
        
    def get_longest_s(self, s, t, l, r):
        length = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            l -=1
            r += 1
        if l < 0 or s[l] not in t:
            return length
        # you still have possibility to extend with t
        rs = [i for i in range(len(t)) if t[i] == s[l]]
        saved_l = l
        longest = length
        saved_length = length
        for r in rs:
            l = saved_l
            length = saved_length
            while l >= 0 and r < len(t) and s[l] == t[r]:
                length += 2
                l -=1
                r += 1
            longest = max(longest, length)
        return longest