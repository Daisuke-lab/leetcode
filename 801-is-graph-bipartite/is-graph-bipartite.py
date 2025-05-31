class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.red = set()
        self.blue = set()
        self.visited = set()
        self.ad_list = graph
        n = len(graph)
        for i in range(n):
            if i not in self.visited and self.dfs(i, "red") is False:
                return False
        return True
        
    def dfs(self, node, color):
        if color == "red" and node in self.blue:
            return False
        elif color == "blue" and node in self.red:
            return False
        if node in self.visited:
            return True
        self.visited.add(node)
        box = self.red if color == "red" else self.blue
        next_color = "blue" if color == "red" else "red"
        box.add(node)
        result = True
        for ad in self.ad_list[node]:
            if self.dfs(ad, next_color) is False:
                return False
        return True