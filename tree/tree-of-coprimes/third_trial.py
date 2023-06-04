import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None, index=0):
        self.val = val
        self.index = index
        self.ancestor_indexes = []
        self.ancestor_values = []
        self.left = left
        self.right = right

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        nodes = self.make_nodes(nums, edges)
        answers = []
        for node in nodes:
            answer = self.get_comprime(node)
            answers.append(answer)

        return answers
            

    
    def get_comprime(self, current):
        for i, ancestor_value in enumerate(current.ancestor_values):
            if math.gcd(ancestor_value, current.val) == 1:
                return current.ancestor_indexes[i]
        return -1 
        

    def make_nodes(self, nums, edges):
        nodes = [None for num in nums]
        for i in range(len(edges)):
            #j, kどちらがchildになるかわからない。
            j, k = edges[i]
            if nodes[j] is None:
                node = TreeNode(nums[j])
                nodes[j] = node
            if nodes[k] is None:
                node = TreeNode(nums[k])
                nodes[k] = node

            if nodes[j].left is None:
                nodes[j].left = nodes[k]
            else:
                nodes[j].right = nodes[k]

            nodes[k].ancestor_values.extend(nodes[j].ancestor_values)
            nodes[k].ancestor_values.append(nodes[j].val)
            nodes[k].ancestor_indexes.extend(nodes[j].ancestor_indexes)
            nodes[k].ancestor_indexes.append(j)
        return nodes
            


