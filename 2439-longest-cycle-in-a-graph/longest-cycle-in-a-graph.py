class Solution:
    # 1 node can be in 1 cycle
    # you need global visited to avoid the duplicates
    # you want path. no need of cycle
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        self.edges = edges
        self.visited = set()
        longest_cycle = -1
        for i in range(n):
            if i not in self.visited:
                path = collections.deque()
                local_visited = set()
                cycle_starting_point = self.find_cycle(i, path, local_visited)
                if cycle_starting_point != -1:
                    cycle = self.trim(path, cycle_starting_point)
                    longest_cycle = max(longest_cycle, len(cycle))
        return longest_cycle


    def trim(self, path, cycle_starting_point):
        while path[0] != cycle_starting_point:
            path.popleft()
        #print(path)
        path.popleft()
        return path


    def find_cycle(self, curr, path, local_visited):
        if curr in local_visited:
            path.append(curr)
            return curr
        if curr in self.visited:
            return -1
        self.visited.add(curr)
        next_node = self.edges[curr]
        path.append(curr)
        local_visited.add(curr)
        #cycle.add(curr)
        if next_node == -1:
            return -1
        else:
            return self.find_cycle(next_node, path, local_visited)
