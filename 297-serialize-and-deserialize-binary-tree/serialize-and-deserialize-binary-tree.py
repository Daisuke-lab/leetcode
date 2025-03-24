# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder = []
        self.inorder = []
        self.inorder_search(root)
        self.preorder_search(root)
        result =  ",".join(self.preorder) + "|" + ",".join(self.inorder)
        #print(result)
        return result
    
    def inorder_search(self, root):
        if root is None:
            return 
        self.inorder_search(root.left)
        self.inorder.append(f"{root.val}#{hash(root)}")
        self.inorder_search(root.right)
    def preorder_search(self, root):
        if root is None:
            return 
        self.preorder.append(f"{root.val}#{hash(root)}")
        self.preorder_search(root.left)
        self.preorder_search(root.right)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "|":
            return None
        preorder, inorder = data.split("|")
        preorder = preorder.split(",")
        inorder = inorder.split(",")
        tree = dummy = TreeNode()
        direction = "left"
        node_map = {}
        while preorder:
            key = preorder.pop(0)
            val = int(key.split("#")[0])
            node = TreeNode(val)
            node_map[key] = node
            if direction == "left":
                tree.left = node
                tree = node
            else:
                tree.right = node
                tree = node
            direction = "left"
            while inorder and inorder[0] in node_map:
                direction = "right"
                parent_key = inorder.pop(0)
                tree = node_map[parent_key]
        return dummy.left
                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))