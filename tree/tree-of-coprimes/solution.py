import math

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        self.graph = self.build_graph(nums, edges)
        self.nums = nums
        self.answers = [-1] * len(nums)
        self.path = {}
        self.visited = {0}
        self.get_comprime(0, 0)
        return self.answers

    def build_graph(self, nums, edges):
        graph = {}
        for edge in edges:
            i, j = edge
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []

            if j not in graph[i]:
                graph[i].append(j)
            if i not in graph[j]:
                graph[j].append(i)
        return graph
            

    
    def get_comprime(self, current, depth):
        closest_depth = -1
        for num in self.path:
            if gcd(self.nums[current], num) == 1:
                if self.path[num] and self.path[num][-1]["depth"] > closest_depth:
                    self.answers[current] = self.path[num][-1]["index"]
                    closest_depth = self.path[num][-1]["depth"]
        
        #nums[k]がdictに定義されてなかったら[]を入れてそこに(k,i)をappend
        #pathには {num: (current (index), depth)}を入れていく。
        self.path.setdefault(self.nums[current], []).append({"index": current, "depth": depth})
        for neighbour in self.graph.get(current, []):
            if neighbour not in self.visited:
                self.visited.add(neighbour)
                self.get_comprime(neighbour, depth+1)
        self.path[self.nums[current]].pop()