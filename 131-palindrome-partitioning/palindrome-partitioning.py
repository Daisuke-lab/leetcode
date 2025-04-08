class Solution:
    # Brute Force => n^3 <= n^2 for iteration, n for checking if it's palindrome
    # odd palindrome n^2
    # even palindrome n^2
    # in total , it's 2n^2
    # But it's hard to separate
    # it's the list of list, so top down
    
    # iterate s and cut s and solve sub problem O(n)
    # for each cutted s, you check if it's palindrome O(n)
    # you are going to add current palindrome to answer O(n)
    # what do you want to memo?
    # memo[i] = palindrome[]
    # then it can not be top down
    # 
    def partition(self, s: str) -> List[List[str]]:
        self.answers = []
        self.s = s
        self.memo = {}
        self.recursion(0, [])
        return self.answers
        
    def recursion(self, i, curr):
        if i == len(self.s):
            self.answers.append(curr.copy())
            return

        for j in range(i, len(self.s)+1):
            if self.is_palindrome(self.s[i:j]):
                curr.append(self.s[i:j])
                self.recursion(j, curr)
                curr.pop()



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