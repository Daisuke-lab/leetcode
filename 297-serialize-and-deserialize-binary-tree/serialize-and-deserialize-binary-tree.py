# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        self.serialized = []
        self.preorder(root)
        print(self.serialized)
        return ",".join(self.serialized)


    def preorder(self, root):
        if root is None:
            self.serialized.append("N")
            return
        self.serialized.append(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)

        
        

    def deserialize(self, data):
        self.vals = data.split(",")
        self.i = 0
        return self.dfs()
    
    def dfs(self):
        if self.vals[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(self.vals[self.i]))
        self.i += 1
        node.left = self.dfs()
        node.right = self.dfs()
        return node

                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))