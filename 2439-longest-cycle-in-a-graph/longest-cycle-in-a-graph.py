class Solution:
    # create ad_list
    # dfs from unvisited node (find cycle)
    # trim 
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        self.ad_list = self.init_ad_list(n, edges)
        #print(self.ad_list)
        self.explored = set()
        max_length = -1
        for node in range(n):
            if node not in self.explored:
                path = collections.deque()
                meeting_point = self.find_cycle(node, set(), path)
                #print(meeting_point)
                if meeting_point != -1:
                    length = self.trim(meeting_point, path)
                    max_length = max(max_length, length)
        return max_length

    def trim(self, meeting_point, path):
        while path[0] != meeting_point:
            path.popleft()
        return len(path)
    
    def find_cycle(self, node, curr_visited, path):
        if node in curr_visited:
            return node
        if node in self.explored:
            return -1
        curr_visited.add(node)
        path.append(node)
        self.explored.add(node)
        for ad in self.ad_list[node]:
            meeting_point = self.find_cycle(ad, curr_visited, path)
            if meeting_point != -1:
                return meeting_point
        
        curr_visited.remove(node)
        del path[-1]
        return -1

    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in enumerate(edges):
            if v2 != -1:
                ad_list[v1].add(v2)
        return ad_list