class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        set_a = set([])
        set_b = set([])

        current_set = set_b
        for current_node, neighbours in enumerate(graph):
            if current_node in set_a:
                set_b.update(neighbours)
            elif current_node in set_b:
                set_a.update(neighbours)
            else:
                current_set.update(neighbours)
            current_set = set_b if current_set == set_a else set_a

        print(set_a)
        print(set_b)
        print(set_a & set_b)
        print(len(set_a & set_b))
        return len(set_a & set_b) == 0