import math
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        self.graph = self.create_graph(n, threshold)
        answers = []
        for start, dest in queries:
            answers.append(self.is_connected(start, dest))

        return answers

    #ここを工夫しないとtime limit exceededになってしまう。
    def create_graph(self, n, threshold):
        graph = {}
        for i in range(1, n + 1):
            neighbours = []
            for j in range(1, n + 1):
                gcd = math.gcd(i, j)
                if gcd > threshold and i != j:
                    neighbours.append(j)
            graph[i] = neighbours
        return graph
                

    def is_connected(self, start, dest):
        visited = []
        queue = [start]
        while len(queue) != 0:
            current = queue.pop()
            if current == dest:
                return True
            else:
                visited.append(current)
                for neighbour in self.graph[current]:
                    if  neighbour not in visited:
                        queue.append(neighbour)

        return False