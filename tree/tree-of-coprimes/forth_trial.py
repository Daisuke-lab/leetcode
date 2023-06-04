import math

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        self.graph = self.build_graph(nums, edges)
        print(self.graph)
        self.nums = nums
        answers = []
        for node in self.graph.keys():
            visited = []
            answer = self.get_comprime(node, visited)
            answers.append(answer)

        return answers

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
            

    
    def get_comprime(self, start_node, visited):
        queue = [start_node]
        while len(queue) > 0:
            node = queue.pop()
            print(self.nums[start_node], self.nums[node])
            if node == 0:
                -1
            elif node in visited:
                pass
                return node
            else:
                visited.append(node)
                for neigbour in self.graph[node]:
                    queue.append(neigbour)
        return -1