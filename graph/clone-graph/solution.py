"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        return self.clone(node)

    def clone(self, node):
        if node is None:
            return None
        if node.val in self.visited:
            return self.visited[node.val]
        else:
            cloned_node = Node(node.val)
            self.visited[node.val] = cloned_node
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(self.clone(neighbor))
            return cloned_node

