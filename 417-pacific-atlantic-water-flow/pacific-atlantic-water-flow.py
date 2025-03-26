class Solution:
    # DP
    # you can mark the position as pacific_reachable, atlantic_reachable
    # once you reach the cell, it means you don't have to go through it again
    # you go through every poisition and check if it can be reachable to both oceans
    # Let's define another function
    # the output should be pacific_reachable, atlantic_reachable
    # before propagating, please check the height and index range
    # args would be (i, j)
    # you can cache tab[i][j] = pacific_reachable, atlantic_reachable

    # when it's the same height, the consequence changes based on visited.
    # but at the same time, you want to prevent infinite loop
    # If it's the same height, you can pass ad_reachable as args
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.ROW = len(self.heights)
        self.COL = len(self.heights[0])
        self.tab = [[None for j in range(self.COL)] for i in range(self.ROW)]
        answer = []
        for i in range(self.ROW):
            for j in range(self.COL):
                if (i, j) == (3, 27):
                    print(self.tab[3][27])
                pacific_reachable, atlantic_reachable = self.is_reachable(i, j, set(), False, False)
                if (i, j) == (3, 27):
                    print(pacific_reachable, atlantic_reachable)
                if pacific_reachable and atlantic_reachable:
                    answer.append([i, j])
        return answer

    def is_reachable(self, i, j, passed, prev_pacific_reachable, prev_atlantic_reachable):
        if self.tab[i][j] is not None:
            return self.tab[i][j]
        if (i, j) in passed:
            return False, False
        if (i, j) == (3, 27):
            print(passed, prev_pacific_reachable, prev_atlantic_reachable)
            print("height::", self.heights[i][j])
        pacific_reachable, atlantic_reachable = self.check_edge(i, j)
        pacific_reachable = pacific_reachable or prev_pacific_reachable
        atlantic_reachable = atlantic_reachable or prev_atlantic_reachable
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        passed.add((i, j))
        same_heights = []
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if new_i < 0 or new_i == self.ROW or new_j < 0 or new_j == self.COL:
                continue
            if self.heights[i][j] > self.heights[new_i][new_j]:
                ad_pacific_reachable, ad_atlantic_reachable = self.is_reachable(new_i, new_j, passed, False, False)
            elif self.heights[i][j] == self.heights[new_i][new_j]:
                same_heights.append((new_i, new_j))
                ad_pacific_reachable, ad_atlantic_reachable = (False, False)
            else:
                ad_pacific_reachable, ad_atlantic_reachable = (False, False)
            # if (i, j) == (3, 27):
            #         print(f"new_i:{new_i}, new_j:{new_j}")
            #         print(f"ad_pacific_reachable:{ad_pacific_reachable}, ad_atlantic_reachable={ad_atlantic_reachable}") 
            pacific_reachable = ad_pacific_reachable or pacific_reachable
            atlantic_reachable = ad_atlantic_reachable or atlantic_reachable
        for new_i, new_j in same_heights:            
            ad_pacific_reachable, ad_atlantic_reachable = self.is_reachable(new_i, new_j, passed, pacific_reachable, atlantic_reachable)
            pacific_reachable = ad_pacific_reachable or pacific_reachable
            atlantic_reachable = ad_atlantic_reachable or atlantic_reachable
            # if (i, j) == (0, 0):
            #         print(f"new_i:{new_i}, new_j:{new_j}")
            #         print(f"ad_pacific_reachable:{ad_pacific_reachable}, ad_atlantic_reachable={ad_atlantic_reachable}") 


        passed.remove((i, j))
        self.tab[i][j] = (pacific_reachable, atlantic_reachable)
        return pacific_reachable, atlantic_reachable

    
    def check_edge(self, i, j):
        pacific_reachable = False 
        atlantic_reachable = False
        if i == 0:
            pacific_reachable = True
        if i == self.ROW - 1:
            atlantic_reachable = True
        if j == 0:
            pacific_reachable = True 
        if j == self.COL -1:
            atlantic_reachable = True

        return (pacific_reachable, atlantic_reachable)
        
        