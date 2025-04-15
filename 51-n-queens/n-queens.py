class Solution:
    # Brute Force
    # 1. Put one queen
    # 2. mask overlapped position
    # 3. recursion
    # O(n^3)

    # Clever solution
    # 1. iterate 1 row, put queen anywhere
    # 2. generate next row with masking
    # 
    # O(n^2)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.positions_list = []
        self.n = n
        self.recursion(set(), set(), set(), [], 0)
        answer_list = []
        for positions in self.positions_list:
            answer = []
            for i, j in positions:
                s = "".join(["Q" if k == j else "." for k in range(n)])
                answer.append(s)
            answer_list.append(answer)
        return answer_list


    def recursion(self, out_col, out_dig_left, out_dig_right, positions, i):
        if i == self.n:
            self.positions_list.append(positions.copy())
        for j in range(self.n):
            dig_left = i + j
            dig_right = i - j
            if j not in out_col and dig_left not in out_dig_left and dig_right not in out_dig_right:
                positions.append((i, j))
                out_col.add(j)
                out_dig_left.add(dig_left)
                out_dig_right.add(dig_right)
                self.recursion(out_col, out_dig_left, out_dig_right, positions, i + 1)
                positions.pop()
                out_col.remove(j)
                out_dig_left.remove(dig_left)
                out_dig_right.remove(dig_right)


