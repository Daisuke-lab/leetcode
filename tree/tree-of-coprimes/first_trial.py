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
        # answers = []
        # while len(self.queue) > 0:
        #     current = queue.pop(0)
        #     answer = self.get_comprime(current)
        #     ans.append(answer)

        # return answer
            

    
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
        while len(edges) > 0:
            edge = edges[0]
            if root.index == edge[0]:
                edge = edges.pop(0)
                child_index = edge[1]
                child_value = nums[child_index]
                child = TreeNode(child_value, index=child_index)
                if root.left is None:
                    root.left = child
                    root.left.ancestor_indexes.extend(root.ancestor_indexes)
                    root.left.ancestor_indexes.append(root.index)
                    root.left.ancestor_values.extend(root.ancestor_values)
                    root.left.ancestor_values.append(root.val)
                    self.queue.append(root.left)
                else:
                    root.right = child
                    root.right.ancestor_indexes.extend(root.ancestor_indexes)
                    root.right.ancestor_indexes.append(root.index)
                    root.right.ancestor_values.extend(root.ancestor_values)
                    root.right.ancestor_values.append(root.val)
                    self.queue.append(root.right)
            else:
                i += 1
                if len(self.queue) > i:
                    current = self.queue[i]


        
                

                