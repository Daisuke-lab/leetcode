class TreeAncestor:

    def __init__(self, n: int, parents: List[int]):
        self.max_exponent = ceil(math.log(n, 2))
        self.n = n
        # 2^n parent
        # 0 => 2^0 = 1
        # 1 => 2^1 = 2
        self.ancestors = [[
            -1 for i in range(self.max_exponent + 1)]
            for j in range(self.n)]

        for node, parent in enumerate(parents):
            self.ancestors[node][0] = parent
        for exponent in range(self.max_exponent + 1):
            self.ancestors[0][exponent] = -1
        
        for exponent in range(self.max_exponent + 1):
            for node in range(n):
                # prev = 2^(curr - 1)
                # what you want is 2^curr
                # 2^(curr-1)+prev 2^(crr-1) = 2* 2^(curr - 1) = 2^curr
                prev = self.ancestors[node][exponent - 1]
                if prev != -1:
                    self.ancestors[node][exponent] = self.ancestors[prev][exponent - 1]
        

    def getKthAncestor(self, node: int, k: int) -> int:
        binary =bin(k)[2:]
        for i, bit in enumerate(binary):
            # 1100
            # 
            exponent = (len(binary) - (i+1))
            if bit == "1":
                node = self.ancestors[node][exponent]
                if node == -1:
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)