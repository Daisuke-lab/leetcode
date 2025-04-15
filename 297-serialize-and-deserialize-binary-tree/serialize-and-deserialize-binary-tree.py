# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def to_list(self, root, curr):
        if root is None:
            curr.append("N")
            return curr
        curr.append(root.val)
        curr = self.to_list(root.left, curr)
        curr = self.to_list(root.right, curr)
        return curr

    def serialize(self, root):
        return str(self.to_list(root,  []))

    def deserialize(self, data):
        data = data.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
        nums = data.split(",")
        return self.to_tree(nums)
        

    def to_tree(self, nums):
        val = nums.pop(0)
        val = int(val) if val != "N" else None
        if val is None:
            return None
        else:
            root = TreeNode(val)
            root.left = self.to_tree(nums)
            root.right = self.to_tree(nums)
            return root
        #return self.to_tree(data)


                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))