class Solution:
    def countDigitOne(self, n: int) -> int:
        self.n = str(n)
        self.memo = [
            [ 
                [-1 for i in range(2)]
                    for j in range(10)]
                    for i in range(10)]
        result =  self.dp(0, 0, 1)
        return result

    def dp(self, pos, count, tight):
        # out of bound
        if pos == len(self.n):
            return count
        # if feels like count value is duplicated
        if self.memo[pos][count][tight] != -1:
            return self.memo[pos][count][tight]
        limit = int(self.n[pos]) if tight == 1 else  9
        result = 0
        for digit in range(limit + 1):
            curr_count = count + 1 if digit == 1 else count
            if tight == 1 and limit == digit:
                result += self.dp(pos + 1, curr_count, 1)
            else:
                result += self.dp(pos + 1, curr_count, 0)

        self.memo[pos][count][tight] = result
        return result

        