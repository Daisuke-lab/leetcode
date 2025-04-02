class Solution:
    # it can be memo {(s, t): True}, but the value is boolean
    # and you want to return True as soon as you find it
    # so you can make visited as set()
    def isMatch(self, s: str, p: str) -> bool:
        self.visited = set()
        self.s = s
        self.p = p
        i = len(s) - 1
        j = len(p) - 1
        return self.dp(i, j)


    def dp(self, i, j):
        if i == -1 and j == -1:
            return True
        elif i < -1:
            return False
        elif j == -1:
            return False
        elif (i, j) in self.visited:
            return False
        self.visited.add((i, j))
        if self.p[j] == "*":
            if self.p[j-1] == ".":
                if self.dp(i, j-2): return True
                while i >= 0:
                    i -=1
                    result = self.dp(i, j-2) 
                    if result:
                        return True
            else:
                if self.dp(i, j-2): return True
                while i >= 0 and self.s[i] == self.p[j-1]:
                    i -=1
                    result = self.dp(i, j-2) 
                    if result:
                        return True
        elif self.p[j] == ".":
            return self.dp(i-1, j-1)
        elif self.p[j] == self.s[i]:
            return self.dp(i-1, j-1)
        
        return False