class Solution:
    # DFS
    # taken seat is [(i, j)]
    # => Because a student can only see the front row, it can only be j.
    # First, you need to generate all the seat allocation patterns in the row
    # n/3 permutation => sets
    # m^2 * n *  
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.ROW = len(seats)
        self.COL = len(seats[0])
        self.all_seated = (1 << self.COL) - 1
        self.seats = seats
        self.memo = [[
            -1 for i in range(self.ROW)]
                for j in range(self.all_seated)]
        return self.dp(0, 0)
        
    def dp(self, front_seated, i):
        if i == self.ROW:
            return 0
        if self.memo[front_seated][i] != -1:
            return self.memo[front_seated][i]
        row = self.seats[i]
        seat_patterns = set()
        seat_patterns.add((0, 0))
        for j in range(self.COL):
            if self.seats[i][j] == "#":
                continue
            upper_left_seated = (front_seated & 1 << j - 1) != 0 if j != 0 else False
            upper_right_seated = (front_seated & 1 << j + 1) != 0 if j != self.COL - 1 else False
            if not upper_left_seated and not upper_right_seated:
                new_seat_patterns = set()
                for seat_pattern, count in seat_patterns:
                    new_seat_patterns.add((seat_pattern, count))
                    left_seated = (seat_pattern & 1 << j - 1) != 0 if j != 0 else False
                    right_seated = (seat_pattern & 1 << j + 1) != 0 if j != self.COL - 1 else False
                    if not left_seated and not right_seated:
                        new_seat_pattern = seat_pattern | 1 << j
                        new_seat_patterns.add((new_seat_pattern, count + 1))
                seat_patterns = new_seat_patterns
        result = 0
        for seat_pattern, count in seat_patterns:
            result = max(result, self.dp(seat_pattern, i+1) + count)
        self.memo[front_seated][i] = result
        return result