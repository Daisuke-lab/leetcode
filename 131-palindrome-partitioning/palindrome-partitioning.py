class Solution:
    # first you can make all substring n^2
    # and then you can check if it's palindrome O(n)
    # => NO

    # you want to have answer list variable
    # you want to maintain the size
    # parition s[size*rep:size*(rep + 1)]
    # if it's not palindrome, 
    # the answer is the list of list, so you want to use top down
    # then difine another function 
    # What is the base case ?? => if s=="", it's the time when you add answer
    # as args, you want to pass curr
    # n^3
    def partition(self, s: str) -> List[List[str]]:
        self.answer = []
        self.recursion(s, [])
        return self.answer


    def recursion(self, s, curr):
        if s == "":
            self.answer.append(curr.copy())
        size = 1
        while size <= len(s):
            batch = s[:size]
            if self.is_palindrome(batch):
                curr.append(batch)
                next_s = s[size:] if size != len(s) else ""
                self.recursion(next_s, curr)
                curr.pop()
            size += 1
            

    def is_palindrome(self, s):
        if s == "":
            return True
        if s[0] == s[-1]:
            return self.is_palindrome(s[1:-1])
        else:
            False