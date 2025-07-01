class TreeAncestor:

    def __init__(self, n: int, parents: List[int]):
        self.max_exponent = ceil(math.log(n, 2))
        self.ancestors = [[
            -1 for i in range(self.max_exponent + 1)]
            for j in range(n)]
        for node in range(n):
            self.ancestors[node][0] = parents[node]
        for exponent in range(self.max_exponent + 1):
            self.ancestors[0][exponent] = -1
        for exponent in range(self.max_exponent + 1):
            for node in range(n):
                prev = self.ancestors[node][exponent - 1]
                if prev != -1:
                    self.ancestors[node][exponent] = self.ancestors[prev][exponent -1]
         
        

    def getKthAncestor(self, node: int, k: int) -> int:
        binary = bin(k)[2:]
        for i, bit in enumerate(binary):
            exponent = len(binary) - (i + 1)
            if bit == "1":
                node = self.ancestors[node][exponent]
                if node == -1:
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)