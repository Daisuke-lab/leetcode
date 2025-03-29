class Solution:
    # if you scan forward [1,11, 0, 6] <= you don't know what to do with 0
    # if you scane backward [6, 10, 11] or [6, 10, 1, 1]
    # What if 60111?? => Impsossible number so let's check it from backward
    # Is there any way to speed up ?? => you can make memo {s: count}
    # As global variable
    # self.s
    # self.memo 
    # self.count
    # As function
    # decode(c) => integer
    # dp(self, c)
    # if c == "" stop
    # if len(c) == 1, decode and add count
    # if c in memo => add count and stop
    # if c[-1] == 0, => decode the last two, and go to the next recursion with c[:-2]
    # if c[-2] != 0 and c[-2:] < 26 => decode the last two as well
    # decode c[-1] and go to the next recursion
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        self.count = 0
        return self.dp(s)

    def dp(self, s):
        count = 0
        if len(s) == 0:
            return 1
        if len(s) == 1:
            if s[0] != "0":
                return 1
            return 0
        if s in self.memo:
            return self.memo[s]
        
        if int(s[-1]) > 0:
            count += self.dp(s[:-1])
        if int(s[-2]) != 0 and int(s[-2:]) <= 26:
            count += self.dp(s[:-2])
        self.memo[s] = count
        return count




        