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
        self.tab = [0 for i in range(len(s))]
        self.tab[0] = 1 if s[0] != "0" else 0
        if len(s) == 1:
            return self.tab[0]
        # 0, 1 as 2 chars
        if s[1] != "0" and s[0] != "0":
            self.tab[1] += 1
        # 0, 1 as 1 char
        if s[0] != "0" and 0 < int(s[:2]) and int(s[:2]) <= 26:
            self.tab[1] += 1
        if len(s) == 2:
            return self.tab[1]

        for i in range(2, len(s)):
            # If you are not 0, you can add patterns you find 0 ~ i-1
            if s[i] != "0":
                self.tab[i] += self.tab[i-1]
            # you i-1~i can be decoded, you can add patterns you find 0 ~ i-2
            if s[i-1] != "0" and 0 < int(s[i-1:i+1]) and int(s[i-1:i+1]) <= 26:
                self.tab[i] += self.tab[i-2]
        return self.tab[-1]


        