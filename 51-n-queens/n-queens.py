class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # queen is not vertically, horizontaly, diagonaly overlapped.
        # One solution
        # 1. you create a board
        # 2. put queen in open space
        # 3. out the space having conflict
        # 4. call recursion and return the max queen number
        # 5. base case is when all cells are out
        # top down is more natural
        # you want to pass positions=[(i,j)] and taken=[i, j, (i, j)] andas args
        # *you can insert diagonal position to taken but taken is hard to be resued for the next iteration
        # Let's define is_available function to check diagonal line 
        # once you finish the recursion, populate the board
        
        # Put somewhere in the first row 
        # the next row, you can not put the next queen in adjacent column in the previous queen
        # maintain columns
        self.positions_list = []
        self.n = n
        self.recursion(0, set(), set(), set(), [])
        answer = []
        return [["".join(["Q" if (i, j) in positions else "." for j in range(n)]) for i in range(n)] for positions in self.positions_list]
        # for positions in self.positions_list:
        #     answer.append(["".join(["Q" if (i, j) in positions else "." for j in range(n)]) for i in range(n)])
        # return answer
    
    def recursion(self, i, taken_columns, left_invalid, right_invalid, curr):
        if i == self.n:
            self.positions_list.append(curr.copy())
            return
        for j in range(self.n):
            if j in taken_columns:
                continue
            if j + i in left_invalid:
                continue
            if i - j in right_invalid:
                continue
            taken_columns.add(j)
            curr.append((i, j))
            left_invalid.add(j + i)
            right_invalid.add(i - j)
            self.recursion(i+1, taken_columns, left_invalid, right_invalid, curr)
            taken_columns.remove(j)
            curr.pop()
            left_invalid.remove(j + i)
            right_invalid.remove(i - j)

