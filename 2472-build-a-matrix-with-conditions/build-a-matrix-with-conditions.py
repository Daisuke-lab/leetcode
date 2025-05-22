class Solution:
    # sounds like topological sort
    # what is out degree above to below, left to right
    # you need 2 graphs
    # how do you handle cycle? => init all the vertices in conditinos and you can do topological sort. If the cound doesn't match
    # it means there is a cycle
    # how do you put no condition k? => as long as there is no cycle, you can create matrix. create a hashset (1~k) and fill out
    # matrix first and insert the remaining element into "0"
    # how do you combine 2 graphs? => choose 0 incoming from rowgraph and get index of "the node" in colGraph: O(n)
    # 
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_sorted_nodes = self.topological_sort(rowConditions)
        col_sorted_nodes = self.topological_sort(colConditions)
        if row_sorted_nodes is None or col_sorted_nodes is None:
            return []
        num_set = self.init_num_set(k)
        matrix = [[
            0 for i in range(k)]
            for j in range(k)]
        
        for i, node in enumerate(row_sorted_nodes):
            try:
                j = col_sorted_nodes.index(node)
            except:
                j = 0
            matrix[i][j] = node
            num_set.remove(node)
        for j, node in enumerate(col_sorted_nodes):
            if node not in num_set:
                continue
            i = 0
            while matrix[i][j] != 0:
                i += 1
            matrix[i][j] = node
            num_set.remove(node)
            
        remaining_nums = self.get_next_num(num_set)
        for i in range(k):
            for j in range(k):
                if matrix[i][j] == 0:
                    try:
                        matrix[i][j] = next(remaining_nums)
                    except:
                        continue
        return matrix

    def get_next_num(self, num_set):
        for num in num_set:
            yield num

    def init_num_set(self, k):
        num_set = set()
        for i in range(1, k+1):
            num_set.add(i)
        return num_set

    def topological_sort(self, edges):
        nodes = set()
        for v1, v2 in edges:
            nodes.add(v1)
            nodes.add(v2)
        out_list = self.init_out_list(nodes, edges)
        in_list = self.init_in_list(nodes, edges)
        zero_incomings = self.collect_zero_incomings(in_list)
        sorted_nodes = []
        while zero_incomings:
            node = zero_incomings.popleft()
            sorted_nodes.append(node)
            for ad in out_list[node]:
                in_list[ad].remove(node)
                if len(in_list[ad]) == 0:
                    zero_incomings.append(ad)
        if len(sorted_nodes) == len(nodes):
            return sorted_nodes
        else:
            return None

    def collect_zero_incomings(self, in_list):
        zero_incomings = collections.deque()
        for node in in_list:
            if len(in_list[node]) == 0:
                zero_incomings.append(node)
        return zero_incomings

        
    def init_out_list(self, nodes, edges):
        out_list = {node: set() for node in nodes}
        for v1, v2 in edges:
            out_list[v1].add(v2)
        return out_list
    
    def init_in_list(self, nodes, edges):
        in_list = {node: set() for node in nodes}
        for v1, v2 in edges:
            in_list[v2].add(v1)
        return in_list
        