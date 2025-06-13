class Solution:
    # you have 2 choices
    # include 
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.s = s
        self.memo = {}
        self.recursion(0, [])
        return self.answer


    def recursion(self, i, curr):
        if i == len(self.s):
            if curr and self.is_palindrome(curr[-1]):
                self.answer.append(curr.copy())
                return
            else:
                return 
        if not curr or self.is_palindrome(curr[-1]):
            curr.append(self.s[i])
            self.recursion(i+1, curr)
            del curr[-1]
        if curr:
            original = curr[-1]
            original_index = len(curr) - 1
            curr[-1] += self.s[i]
            self.recursion(i+1, curr)
            curr[original_index] = original 


    def is_palindrome(self, s):
        result = False
        if s == "":
            result =  False
        elif len(s) == 1:
            result =  True
        elif len(s) == 2 and s[0] == s[-1]:
            result =  True
        elif s in self.memo:
            return self.memo[s]
        elif s[0] == s[-1]:
            result =  self.is_palindrome(s[1:-1])
        self.memo[s] = result
        return result