class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.locked = False
        self.locking_user = None

class LockingTree:

    def __init__(self, parent: List[int]):
        self.root = TreeNode(0)
        current = self.root
        self.make_tree(parent, current)


    def make_tree(self, parent, current):
        for i, parent_value in enumerate(parent):
            if current.val == parent_value:
                if current.left is None:
                    current.left = TreeNode(i)
                    self.make_tree(parent, current.left)
                else:
                    current.right = TreeNode(i)
                    self.make_tree(parent, current.right)

    def lock(self, num: int, user: int) -> bool:
        node = self.find_node(self.root, num)
        if node.locked is False:
            node.locked = True
            node.locking_user = user
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        node = self.find_node(self.root, num)
        if node.locked and node.locking_user == user:
            node.locked = False
            node.locking_user = None
            return True
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        node = self.find_node(self.root, num)
        has_locked_child = self.has_locked_child(node)
        has_locked_parent = self.has_locked_parent(self.root, node)
        print(node.locked, has_locked_child, has_locked_parent)
        #
        if node.locked == False and has_locked_child and has_locked_parent is False:
            self.unlock_children(node)
            node.locked = True
            node.locked_user = num
            return True
        return False

    def find_node(self, root, num):
        if root is None:
            return
        elif root.val == num:
            return root
        else:
            left_node = self.find_node(root.left, num)
            if left_node is not None:
                return left_node
            
            right_node = self.find_node(root.right, num)
            if right_node is not None:
                return right_node

    def has_locked_child(self, root):
        if root is None:
            return False
        elif root.locked:
            return True
        else:
            return self.has_locked_child(root.left) or self.has_locked_child(root.right)


    def has_locked_parent(self, root, node):
        def search(root):
            nonlocal reached, found
            if root is None:
                return False
            elif root == node:
                reached = True
                return found
            elif reached:
                return found
            elif found:
                return True
            elif root.locked:
                found = True
                return True
            else:
                left = search(root.left)
                right = search(root.eight)

        reached = False
        found = False
        search(root)
        return found

    def unlock_children(self, root):
        if root is None:
            return
        elif root.locked:
            root.locked = False
            root.locked_user = None
        self.unlock_children(root.left)
        self.unlock_children(root.right)

                
