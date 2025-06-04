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
        curr.append(str(root.val))
        self.to_list(root.left, curr)
        self.to_list(root.right, curr)
        return curr

    def serialize(self, root):
        return ",".join(self.to_list(root, []))

    def deserialize(self, data):
        print(data)
        preorder = data.split(",")
        return self.to_tree(preorder)[0]

    def to_tree(self, nums, i=0):
        if i >= len(nums):
            return None, i
        if nums[i] == "N":
            i += 1
            return None, i
        node = TreeNode(int(nums[i]))
        i += 1
        node.left, i = self.to_tree(nums, i)
        node.right, i = self.to_tree(nums, i)

        return node, i
        #return self.to_tree(data)


                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))