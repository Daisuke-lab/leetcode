class Solution:
    # available value in the first digit: 1 ~ 3, 1 ~ 13
    # after the character you can do anything, but make sure if it's in range
    # let's say first digit is k. It has to be length + k -1 < 9, otherwise number will be overflow

    # Btw, it returns the list and still uses DP
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.answers = []
        self.low = str(low)
        self.high = str(high)
        self.gap = len(self.high) - len(self.low)
        # print("N:", len(self.high))
        # print("GAP:",self.gap)
        self.low = "0" * self.gap + self.low
        low_tight = True if self.gap == 0 else False
        high_tight = True
        self.recursion(0, "", low_tight, high_tight)
        return self.answers
        
    def recursion(self, pos, curr, low_tight, high_tight):
        if pos == len(self.high):
            #print(curr)
            self.answers.append(int(curr))
            return
        # when you already reach 9 before the last digit
        if curr and curr[-1] == "9":
            return
        start, end = 0, 9
        if low_tight:
            start = int(self.low[pos])
        if high_tight:
            end = int(self.high[pos])
        prev_digit = int(curr[-1]) if len(curr) > 0 else None
        leading_zeros = len(curr) if curr and curr[-1] == "0" else 0
        if self.gap > 0 and leading_zeros == self.gap:
            low_tight = True
            start = int(self.low[pos])

        if leading_zeros > 0 or prev_digit is None:
            for digit in range(start, end + 1):
                next_low_tight = False
                next_high_tight = False
                if low_tight and digit == start:
                    next_low_tight = True
                if high_tight and digit == end:
                    next_high_tight = True
                self.recursion(pos + 1, curr + str(digit), next_low_tight, next_high_tight)
        else:
            digit = prev_digit + 1
            if digit < start or digit > end:
                return
            next_low_tight = True if low_tight and digit == start else False
            next_high_tight = True if high_tight and digit == end else False
            self.recursion(pos + 1, curr + str(digit), next_low_tight, next_high_tight)

            


        
        

        