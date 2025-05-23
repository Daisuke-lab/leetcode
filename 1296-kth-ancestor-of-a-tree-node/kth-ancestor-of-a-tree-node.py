class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.max_exponent = ceil(math.log(n, 2)) + 1
        self.ancestors = [[
            -1 for i in range(self.max_exponent)]
            for j in range(n)]
        self.parents = parent

        for node in range(n):
            self.ancestors[node][0] = self.parents[node]
        for exponent in range(self.max_exponent):
            self.ancestors[0][exponent] = -1

        for exponent in range(1, self.max_exponent):
            for node in range(1, n):
                # the 2^n-1 parent of node
                # the 2^n-1 parent of the 2^n-1 parent
                # (2^(x-1)) + (2^(x-1)) = (2^(x))
                prev = self.ancestors[node][exponent -1]
                if prev != -1:
                    curr = self.ancestors[prev][exponent -1]
                    self.ancestors[node][exponent] = curr



    def getKthAncestor(self, node: int, k: int) -> int:
        # collect exponents
        # k = 2^n + 2^m + 2^s + .....
        # e.g. k = 6 = 4 + 2 => 2^2 + 2^1 => takes 2 jumps and 1 jump from there
        binary = bin(k)[2:]
        curr = node
        for i, bit in enumerate(binary):
            if bit == "1":
                exponent = len(binary) - i -1
                curr = self.ancestors[curr][exponent]
                if curr == -1:
                    return -1
        return curr

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)