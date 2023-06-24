class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        # 0が初期値。1, -1で2groupsに分ける。
        colors = [0] * n

        for i in range(n):
            if colors[i] == 0:
                if not self.dfs(graph, colors, i, 1):
                    return False

        return True

    def dfs(self, graph, colors, node, color):
        #初期値でないとき
        if colors[node] != 0:
            #neighbourとは別のcolorであるべき。
            return colors[node] == color
        else:
            #初期値の時はrecursionよりneighbourとは別のcolorを付与する。
            colors[node] = color

        for neighbor in graph[node]:
            if self.dfs(graph, colors, neighbor, -color) is False:
                return False

        return True