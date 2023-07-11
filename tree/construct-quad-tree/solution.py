"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        self.n = len(grid)

        if self.n == 1:
            return Node(val=self.grid[0][0], isLeaf=True)
        else:
            root = current = Node(val=0, isLeaf=False)
            self.recursion(0, 0, self.n, current)
            return root

    def recursion(self, i, j, width, root):

        if self.is_mono_grid(i, j, width):
            root.isLeaf = True
            root.val = self.grid[i][j]
        else:
            root = self.init_quad(root)
            new_width = width // 2
            
            top_left_i = i
            top_left_j = j

            top_right_i = i
            top_right_j = j + new_width

            bottom_left_i = i + new_width
            bottom_left_j = j

            bottom_right_i = i + new_width
            bottom_right_j = j + new_width

            self.recursion(top_left_i, top_left_j, new_width, root.topLeft)
            self.recursion(top_right_i, top_right_j, new_width, root.topRight)
            self.recursion(bottom_left_i, bottom_left_j, new_width, root.bottomLeft)
            self.recursion(bottom_right_i, bottom_right_j, new_width, root.bottomRight)

        

    def init_quad(self, root):
        root.topLeft = Node(val=0, isLeaf=False)
        root.topRight = Node(val=0, isLeaf=False)
        root.bottomLeft = Node(val=0, isLeaf=False)
        root.bottomRight = Node(val=0, isLeaf=False)

        return root

    def is_mono_grid(self, start_col, start_row, width):
        value = None
        for i in range(start_col, start_col + width):
            for j in range(start_row, start_row + width):
                if value is None:
                    value = self.grid[i][j]
                elif value != self.grid[i][j]:
                    return False

        return True

            
                
        
        