class Solution:
    # memo
    # pos, curr, tight
    # curr: sum
    # if pos == len(n), check if it's bigger than min_sum return 1
    # check tight
    # for loop: 0 to 9 if not tight. if tight num1[pos] to num2[pos]
    # if sum + num <= recursion

    # 01, 12 1 => tight 0 ~ 2
    # untight, num1_tight, num2_tight, both_tight
    # if both_tight =>  num1[pos] to num2[pos]
    # if num2_tight => 0 to num2[pos]
    # if num1_tight => num1[pos] to 9

    # 01 <= num1_tight if gap == pos +1 and curr == 0

    # it has duplicate numbers
    # OR it counts out of bound numbers

    # 000*
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        self.gap = len(num2) - len(num1)
        #print("GAP:", self.gap)
        self.num1 = self.gap * "0" + num1
        self.num2 = num2
        self.min_sum= min_sum
        self.max_sum = max_sum
        self.memo = [[[
            -1 for k in range(4)]
            for j in range(self.max_sum + 1)]
            for i in range(32)]

        tight = 2 if self.gap > 0 else 3
        return self.dp(0, 0, tight, "") % (10**9 + 7)

    def dp(self, pos, curr, tight, num):
        #print(pos, curr, tight, num)
        if pos == len(self.num2):
            if self.min_sum <= curr and curr <= self.max_sum:
                #print(num, curr)
                return 1
            else:
                return 0
        if curr > self.max_sum:
            return 0
        if self.memo[pos][curr][tight] != -1:
            return self.memo[pos][curr][tight]
        start, end = 0, 0
        if tight == 0:
            start, end = 0, 9
        elif tight == 1:
            start = int(self.num1[pos])
            end = 9
        elif tight == 2:
            start = 0
            end = int(self.num2[pos])
        else:
            start = int(self.num1[pos])
            end = int(self.num2[pos])
            
        result = 0
        for digit in range(start, end + 1):
            next_tight = 0
            if curr == 0 and self.gap != 0 and self.gap == pos + 1 and digit == 0:
                next_tight = 1
            else:
                if (tight == 1 or tight == 3) and digit == start:
                    next_tight = 1
                if (tight == 2 or tight == 3)and digit == end:
                    next_tight = 2
                if tight == 3 and start == end:
                    next_tight = 3
            new_num = num +str(digit)
            result += self.dp(pos + 1, curr + digit, next_tight, new_num)
        self.memo[pos][curr][tight] = result
        return result