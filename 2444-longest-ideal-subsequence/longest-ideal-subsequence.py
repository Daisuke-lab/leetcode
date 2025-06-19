class Solution:
    # you want to jump one by one
    # you want to maintain the prev chosen value
    
    # when you have none in prev
    # => you pick up current one
    # when you have prev and it meets the requirement
    # => you include it
    # => you can discard curr
    # when you have prev and it dosen't meet the requirement
    # => you discard curr
    # => you discard prev

    # base case
    # when the last char, it's 1

    # args: i, prev
    # output: max_length

    # you keep abcdefg as key and length of value
    # check around k and pick up the max and + 1

    # n*k
    def longestIdealString(self, s: str, k: int) -> int:
        self.s = s
        self.k = k
        self.memo = [0 for i in range(26)]
        max_length = 0
        for c in self.s:
            i = self.get_index(c)
            length = self.get_max_length(i) + 1
            self.memo[i] = length
            max_length = max(max_length, length)
        return max_length


    def get_max_length(self, i):
        start = max(i - self.k, 0)
        end = min(i+self.k,  25)
        max_length = max(self.memo[start:end+1])
        return max_length

    def get_index(self, c):
        return ord(c) - ord("a")