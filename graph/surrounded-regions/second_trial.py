class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.valid = True

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.col_num = len(board)
        self.row_num = len(board[0])
        self.node_board = [[None for j in range(self.row_num)] for i in range(self.col_num)]


        for i in range(self.col_num):
            for j in range(self.row_num):
                if self.board[i][j] == "O":
                    self.node_board[i][j] = Node(self.board[i][j])
                    self.validate_region(i, j)
                    self.union_neighbour(i, j)
                    
        print(self.node_board)
        self.flip()


    def flip(self):
        for i in range(self.col_num):
            for j in range(self.row_num):
                if self.board[i][j] == "O" and self.node_board[i][j].parent.valid:
                    self.board[i][j] = "X"


    
    def validate_region(self, i, j):
        current_node = self.node_board[i][j]
        if i == 0 or i == self.col_num -1:
            parent = self.find(current_node)
            parent.valid = False

        if j == 0 or j == self.row_num - 1:
            parent = self.find(current_node)
            parent.valid = False
    
                

    def find(self, node):
        if node.parent != node:
            #今のnodeのparentをparentのparentに変更する。
            node.parent = self.find(node.parent)
        return node.parent


    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            #とりあえずrootだけ変える。
            valid = parent2.valid and parent1.valid
            parent2.parent = parent1
            parent1.valid = valid

        return parent1

    def union_neighbour(self, i, j):
        current_node = self.node_board[i][j]

        if i > 0 and self.node_board[i-1][j] is not None:
            self.union(current_node, self.node_board[i-1][j])
        
        if i < self.col_num -2 and self.node_board[i+1][j] is not None:
            self.union(current_node, self.node_board[i+1][j])

        if j > 0 and self.node_board[i][j-1] is not None:
            self.union(current_node, self.node_board[i][j-1])

        if j < self.row_num -2 and self.node_board[i][j+1] is not None:
            self.union(current_node, self.node_board[i][j+1])
        

    



        