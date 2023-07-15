# 400 /800 test cases位を突破する。
#ただ複雑だし、あんまりよくない。
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = self.build_graph(edges)
        edge_objects = self.build_edge_objects(edges)
        distance, through = self.get_shortest_distance(graph, source, destination)

        if distance is None:
            return []

        # if target > distance:
        #     return []
        else:
            last_negative_edge_index = None
            gap = target - distance
            for i in range(len(through)-1):
                
                edge = [through[i], through[i+1]]
                if f"{edge[0]}_{edge[1]}" in edge_objects:
                    edge_index = edge_objects[f"{edge[0]}_{edge[1]}"]
                elif f"{edge[1]}_{edge[0]}" in edge_objects:
                    edge_index = edge_objects[f"{edge[1]}_{edge[0]}"]
                edge = edges[edge_index]
                weight = edge[2]
                if weight == -1:
                    if gap <= 0:
                        return []
                    else:
                        last_negative_edge_index = edge_index
                        edges[edge_index][2] = 1
                        gap = gap - 2
            if last_negative_edge_index is None:
                return []
            else:
                edges[last_negative_edge_index][2] += gap
                self.remove_negative_weights(edges)
                return edges
            

                
            



    def build_graph(self, edges):
        graph = {}
        for node1, node2, weight in edges:
            node1_as_neighbour = {"node": node1, "weight": weight}
            node2_as_neighbour = {"node": node2, "weight": weight}
            if node1 not in graph:
                graph[node1] = [node2_as_neighbour]
            else:
                graph[node1].append(node2_as_neighbour)
            if node2 not in graph:
                graph[node2] = [node1_as_neighbour]
            else:
                graph[node2].append(node1_as_neighbour)

        return graph

    def get_shortest_distance(self, graph, source, destination):
        visited = []
        queue = [{"node": source, "distance": 0, "through": []}]
        while len(queue) > 0:
            info = queue.pop()
            
            node, distance, through = info["node"], info["distance"], info["through"]
            visited.append(node)
            through.append(node)
            if node == destination:
                return [distance, through]

            else:
                for neighbour in graph[node]:
                    if neighbour["node"] not in visited:
                        queue.append({
                            "node":neighbour["node"],
                            "distance": distance + neighbour["weight"],
                            "through": through
                        })
        return None, None


    def build_edge_objects(self,edges):
        edge_objects = {}
        for index, edge in enumerate(edges):
            node1, node2, weight = edge
            key =f"{node1}_{node2}"
            edge_objects[key] = index

        return edge_objects

    def remove_negative_weights(self, edges):
        for i, edge in enumerate(edges):
            edges[i][2] = edges[i][2] if edges[i][2] > 0 else 1
        return edges
            
                    

