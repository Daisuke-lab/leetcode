class UnionFind:
    def __init__(self):
        self.parent = {}
        # you want to put actual value to self.weight like a = 2.0 or b = 3.0 (not division)
        self.weight = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
    
    def find(self, x):
        if x != self.parent[x]:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            # bigger value (e.g. a) is a child and smaller value at the root
            # So you are going to multiply by parent weight
            # * you have to do this as a last step because all the weight need to be updated from the root before you udpate x
            self.weight[x] *= self.weight[orig_parent]
        return self.parent[x]
    
    def union(self, x, y, value):
        self.add(x)
        self.add(y)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            # 1. a/b=2 => a = 2, b = 1, but "b" is the root!
            # 2. b/c=3 => b=3, c = 1
            # => next time you find(), you have to update a to 6, so that a/b is still true
            # 
            self.weight[root_x] = value * self.weight[y] / self.weight[x]
    
    def get_ratio(self, x, y):
        if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
            return -1.0
        return self.weight[x] / self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        
        for (a, b), value in zip(equations, values):
            uf.union(a, b, value)
        #print(uf.weight)
        
        result = [uf.get_ratio(a, b) for a, b in queries]
        #print(uf.weight)
        return result