class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.component_count = n
    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node

    def union(self, v1, v2):
        v1_parent = self.find(v1)
        v2_parent = self.find(v2)
        if v1_parent == v2_parent:
            return 
        if self.size[v1_parent] >= self.size[v2_parent]:
            self.parents[v2_parent] = v1_parent
            self.size[v1_parent] += self.size[v2_parent]
        else:
            self.parents[v1_parent] = v2_parent
            self.size[v2_parent] += self.size[v1_parent]
        self.component_count -= 1

class Solution:
    # it checks if it's all connected (traverse from anywhere to anywhere)
    # union find. the edge exist if gcd > 1:
    # n^2 * log(min(a,b))
    # does it have to be gcd? 
    # 2,3,5,30

    # Then it's DP. 
    # 
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        node_map = {}
        union_find = UnionFind(len(nums))
        for i, num in enumerate(nums):
            primes = self.get_primes(num)
            #print(primes)
            for prime in primes:
                if prime in node_map:
                    union_find.union(i, node_map[prime])
                else:
                    node_map[prime] = i
        return union_find.component_count == 1

    def get_primes(self, num):
        primes = set()
        for i in range(2, ceil(math.sqrt(num)) + 2):
            while num % i == 0:
                num //= i
                primes.add(i)
        if num != 1:
            primes.add(num)
        return primes