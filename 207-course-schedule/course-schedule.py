class Solution:
    # prerequisite => main class
    # do topological sort
    # if the number is the same, return true
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = prerequisites
        n = numCourses
        in_list, out_list = self.init_ad_list(n, edges)
        zero_incomings = self.get_zero_incomings(in_list)
        visited = set()
        while zero_incomings:
            node = zero_incomings.popleft()
            visited.add(node)
            for ad in out_list[node]:
                in_list[ad].remove(node)
                if len(in_list[ad]) == 0:
                    zero_incomings.append(ad)
        return len(visited) == n
        
    def get_zero_incomings(self, in_list):
        zero_incomings = collections.deque()
        for node in in_list.keys():
            if len(in_list[node]) == 0:
                zero_incomings.append(node)
        return zero_incomings

    def init_ad_list(self, n, edges):
        in_list = {i: set() for i in range(n)}
        out_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            in_list[v1].add(v2)
            out_list[v2].add(v1)
        return in_list, out_list