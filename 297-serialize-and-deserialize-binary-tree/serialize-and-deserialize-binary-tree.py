# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def to_map(self, root):
        if root is None:
            return {}
        else:
            return {"val": root.val, "left": self.to_map(root.left), "right": self.to_map(root.right)}
    def serialize(self, root):
        return str(self.to_map(root))

    def deserialize(self, data):
        #print(data)
        return self.to_tree(data)

    def to_tree(self, data):
        if data == "{" + "}":
            return None
        val, i = self.get_val(data)
        left_data, i = self.get_next_data(data, i)
        right_data, i = self.get_next_data(data, i)
        node = TreeNode(val)
        node.left = self.to_tree(left_data)
        node.right = self.to_tree(right_data)
        return node

    def get_val(self, data):
        val_prefix = "{'val': "
        i = len(val_prefix)
        str_num = ""
        is_negative = False
        while True:
            try:
                str_num += str(int(data[i]))
                i += 1
            except:
                if data[i] == "-":
                    is_negative = True
                    i += 1
                else:
                    break
        num = int(str_num)
        num = -num if is_negative else num
        return ( num, i )

    def get_next_data(self, data, i):
        while data[i] != "{":
            i += 1
        start = i
        i += 1
        open_count = 1
        close_count = 0
        while open_count != close_count:
            if data[i] == "{":
                open_count += 1
            if data[i] == "}":
                close_count += 1
            i += 1
        return (data[start:i], i)
        
                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))