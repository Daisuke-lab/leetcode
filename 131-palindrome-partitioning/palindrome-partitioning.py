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
        return self.recursion(0)
        
    def recursion(self, i):
        answer = []
        for j in range(i, len(self.s)+1):
            if self.is_palindrome(self.s[i:j]):
                if j == len(self.s):
                    answer.append([self.s[i:j]])
                sub_answers = self.recursion(j)
                for sub_answer in sub_answers:
                    sub_answer.insert(0, self.s[i:j])
                    answer.append(sub_answer)
        return answer



    def is_palindrome(self, s):
        if s == "":
            return False
        elif len(s) == 1:
            return True
        elif len(s) == 2 and s[0] == s[-1]:
            return True
        elif s[0] == s[-1]:
            return self.is_palindrome(s[1:-1])
        return False