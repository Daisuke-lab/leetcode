class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nodes = {} # {num: node}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                parent = None
                if num + 1 in nodes:
                    parent = self.union(node, nodes[num+1])
                if num - 1 in nodes:
                    parent = self.union(node, nodes[num-1])
                size = parent.size if parent is not None else 1
                max_size = max(max_size, size)
        return max_size

    def find(self, node):
        if node.parent != node:
            #今のnodeのparentをparentのparentに変更する。
            node.parent = self.find(node.parent)
        return node.parent

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            #とりあえずrootだけ変える。
            parent2.parent = parent1
            parent1.size += parent2.size
        return parent1