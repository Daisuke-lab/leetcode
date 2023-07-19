class MyLinkedList:

    def __init__(self, val=-1, _next=None):
        self.val = val
        self.next = _next
        self.root = self

    def get(self, index: int) -> int:
        try:
            current = self.root
            while index > 0:
                index -=1
                current = current.next
            return current.val
        except Exception as e:
            return -1

    def get_node(self, index):
        try:
            current = self.root
            while index > 0:
                index -=1
                current = current.next
            return current
        except:
            return None

    def addAtHead(self, val: int) -> None:
        if self.root.val == -1:
            self.root.val = val
        else:
            new_head = MyLinkedList(val, self.root)
            self.root = new_head

        

    def addAtTail(self, val: int) -> None:
        if self.root.val == -1:
            self.root.val = val
        else:
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = MyLinkedList(val, None)


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        else:
            parent = self.get_node(index-1)
            if parent is not None:
                new_node = MyLinkedList(val, parent.next)
                parent.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.root = self.root.next
        else:
            parent = self.get_node(index -1)
            if parent is not None and parent.next is not None:
                parent.next = parent.next.next