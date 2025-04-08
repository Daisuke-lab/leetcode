class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        s_set = set(s)
        t_set = set(t)
        if len(s_set) == 1 and len(t_set) == 1:
            if list(s_set)[0] == list(t_set)[0]:
                return len(s) + len(t)

        # Find longest palindrome starting from each pos
        s_pal = self.calc_pal(s, is_s=True)
        t_pal = self.calc_pal(t, is_s=False)

        ans = 1
        for s_pos in range(len(s)):
            for t_pos in range(len(t)-1, -1, -1):
                # Update ans with palindrome from s or t only
                ans = max(ans, s_pal[s_pos], t_pal[t_pos])

                s_l, t_r = s_pos, t_pos
                while s_l < len(s) and t_r >= 0:
                    if s[s_l] == t[t_r]:
                        s_l += 1
                        t_r -= 1
                        common_len = s_l - s_pos
                        ans = max(ans, 2 * common_len)
                        if s_l < len(s):
                            ans = max(ans, 2 * common_len + s_pal[s_l])
                        if t_r >= 0:
                            ans = max(ans, 2 * common_len + t_pal[t_r])
                    else:
                        break
        return ans

    def calc_pal(self, string, is_s):
        n = len(string)
        pal = [1] * n
        for i in range(n):
            even_l, even_r = self.max_palindrome(string, i, is_even=True)
            even_len = even_r - even_l + 1
            if is_s:
                pal[even_l] = max(pal[even_l], even_len)
            else:
                pal[even_r] = max(pal[even_r], even_len)
        
            odd_l, odd_r = self.max_palindrome(string, i, is_even=False)
            odd_len = odd_r - odd_l + 1
            if is_s:
                pal[odd_l] = max(pal[odd_l], odd_len)
            else:
                pal[odd_r] = max(pal[odd_r], odd_len)
        return pal


    def max_palindrome(self, arr, pos, is_even):
        if is_even: # Even case
            l, r = pos, pos+1
        else:
            l, r = pos, pos

        min_l = max_r = pos
        while l >= 0 and r < len(arr):
            if arr[l] == arr[r]:
                min_l = l
                max_r = r
            else:
                break
            l -= 1
            r += 1
        return min_l, max_r