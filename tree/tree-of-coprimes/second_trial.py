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
        self.root = self.make_tree(nums, edges)
        answers = []
        while len(self.queue) > 0:
            current = self.queue.pop(0)
            answer = self.get_comprime(current)
            answers.append(answer)

        return answers
            

    
    def get_comprime(self, current):
        for i, ancestor_value in enumerate(current.ancestor_values):
            if math.gcd(ancestor_value, current.val) == 1:
                return current.ancestor_indexes[i]
        return -1 
        

    def make_tree(self, nums, edges):
        root = TreeNode(nums[0])
        current = root
        self.queue = [root]
        i = 0
        edges = [edge for edge in edges]
        for edge in edges:
            if current.index != edge[0]:
                i += 1
                if len(self.queue) > i:
                    current = self.queue[i]
            if current.index == edge[0]:
                child_index = edge[1]
                child_value = nums[child_index]
                child = TreeNode(child_value, index=child_index)
                if current.left is None:
                    current.left = child
                    current.left.ancestor_indexes.extend(current.ancestor_indexes)
                    current.left.ancestor_indexes.append(current.index)
                    current.left.ancestor_values.extend(current.ancestor_values)
                    current.left.ancestor_values.append(current.val)
                    self.queue.append(current.left)
                else:
                    current.right = child
                    current.right.ancestor_indexes.extend(current.ancestor_indexes)
                    current.right.ancestor_indexes.append(current.index)
                    current.right.ancestor_values.extend(current.ancestor_values)
                    current.right.ancestor_values.append(current.val)
                    self.queue.append(current.right)


