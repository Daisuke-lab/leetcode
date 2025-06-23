class Solution:
    # you want to pass row as bitmask that shows availability
    # how do you handle different student alignment in current row.
    # => you can also pass i and j 
    # when you have available seat
    # case1: you skip it and i + 1
    # case2: take a seat and i + 2
    # => you need two bitmasks (curr, next)
    # O(2^n * 2^n * n * m)
    # args: i, j, bitmask
    # output: the max number of students
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.seats = seats
        self.ROW = len(seats)
        self.COL = len(seats[0])
        self.all_seated = (1 << self.COL) - 1
        self.memo = [[[[
            -1 for a in range(self.all_seated + 1)]
            for b in range(self.all_seated + 1)]
            for c in range(self.COL)]
            for d in range(self.ROW)]
        result =  self.dp(0, 0, 0, 0)
        return result


    def dp(self, i, j, curr_seated, invalid_seats):
        if i >= self.ROW:
            return 0
        elif j >= self.COL:
            new_invalid_seats = 0
            for j in range(self.COL):
                if self.is_next_unavailable(j, curr_seated):
                    new_invalid_seats = (new_invalid_seats | (1 << j))
            return self.dp(i+1, 0, 0, new_invalid_seats)
        elif self.memo[i][j][curr_seated][invalid_seats] != -1:
            return self.memo[i][j][curr_seated][invalid_seats]

        invalid = (invalid_seats & (1 << j)) != 0
        result = 0
        if self.seats[i][j] == "#" or invalid:
            result = self.dp(i, j+1, curr_seated, invalid_seats)
        else:
            new_curr_seated = (curr_seated | (1 << j))
            result = max(result, self.dp(i, j+2, new_curr_seated, invalid_seats) + 1)
            result = max(result, self.dp(i, j+1, curr_seated, invalid_seats))
        self.memo[i][j][curr_seated][invalid_seats] = result
        return result

    def is_next_unavailable(self, j, curr_seated):
        if ((1 << j+1) & curr_seated) != 0:
            return True
        if j > 0 and ((1 << j-1) & curr_seated) != 0:
            return True
        return False