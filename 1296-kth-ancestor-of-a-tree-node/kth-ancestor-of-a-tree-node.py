class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.lift_height = ceil(math.log(n, 2)) + 1
        # anceestor[node][exponent] = 2^exponent parent
        self.ancestors = [[
            -1 for j in range(self.lift_height)]
            for i in range(n)]
            
        # 2^0 = 1, insert your parent with O(1) time
        for node in range(n):
            self.ancestors[node][0] = parent[node]
        # any ancestor of root is defined as -1
        for jump in range(self.lift_height):
            self.ancestors[0][jump] = -1
        for jump in range(1, self.lift_height):
            for node in range(1, n):
                prev = self.ancestors[node][jump - 1]
                if prev != -1:
                    # 2^jump-1 parent of 2^jump-1 parent is 2^jump parent
                    #(2^(x-1)) + (2^(x-1)) = (2^(x))
                    self.ancestors[node][jump] = self.ancestors[prev][jump - 1]
        #print(self.ancestors)


    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.lift_height):
            # if k = 2^i + p
            if k & (1 << i): 
                node = self.ancestors[node][i]
                if node == -1:
                    return -1  # No such ancestor
        return node
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)