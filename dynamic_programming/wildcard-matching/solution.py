class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s)-1, len(p) -1
        self.s = s
        self.p = p
        return self.recursion_with_memo(i, j, {})

    def recursion_with_memo(self, i, j, memo):
        key = (i, j)
        if key in memo:
            return memo[key]
        elif i < 0 and j < 0:
            memo[key] = True
            return True
        elif i < 0 and j >= 0:
            k = j
            while k >= 0 and self.p[k] == "*":
                k -= 1
            
            if k < 0:
                memo[key] = True
                return True
            else:
                memo[key] = False
                return False

        elif i >= 0 and j <0:
            memo[key] = False
            return False

        elif i >= 0 and j >= 0:
            if self.p[j] == "*" and self.recursion_with_memo(i, j-1, memo):
                memo[key] = True
                return True
            if self.p[j] == "*" and self.recursion_with_memo(i-1, j, memo):
                memo[key] = True
                return True

            if (self.p[j] == "?" or self.p[j] == self.s[i]) and self.recursion_with_memo(i-1, j-1, memo):
                memo[key] = True
                return True

            memo[key] = False
            return False