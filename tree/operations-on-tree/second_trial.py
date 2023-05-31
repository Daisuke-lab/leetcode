class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []
        self.locked = False
        self.locking_user = None

class LockingTree:
    #binaryとは限らない。left, right以外にもある。
    def __init__(self, parent: List[int]):
        self.root = TreeNode(0)
        current = self.root
        self.make_tree(parent, current)


    def make_tree(self, parent, current):
        for i, parent_value in enumerate(parent):
            if current.val == parent_value:
                child = TreeNode(i)
                current.children.append(child)
                self.make_tree(parent, child)

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
        print(num)
        if [num, user] == [41, 99]:
            print(node.val)
            print(node.locked, has_locked_child, has_locked_parent)
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
            for child in root.children:
                node = self.find_node(child, num)
                if node is not None:
                    return node

    def has_locked_child(self, root):
        if root is None:
            return False
        elif root.locked:
            return True
        else:
            for child in root.children:
                if self.has_locked_child(child):
                    return True
        return False


    def has_locked_parent(self, root, node):
        def search(root):
            nonlocal reached, found
            if reached:
                return found
            elif root is None:
                return False
            elif root.val == node.val:
                reached = True
                return found
            elif found:
                return True
            elif root.locked:
                if node.val == 41:
                    print("locked::", root.val)
                found = True
                return True
            else:
                for child in root.children:
                    search(child)

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
        for child in root.children:
            self.unlock_children(child)
