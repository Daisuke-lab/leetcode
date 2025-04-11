class DoublyLinkedNode():
    def __init__(self):
        self.prev = None
        self.next = None
        self.value = None
        self.key = None

    def build(self):
        tail = self
        head = DoublyLinkedNode()
        tail.next = head
        head.prev = tail
        return tail, head

class LRUCache:

    def __init__(self, capacity: int):
        self.tail, self.head = DoublyLinkedNode().build()
        self.node_map = {}
        self.capacity = capacity


    def remove(self, node):
        if node != self.tail or node != self.head:
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.node_map[node.key]


    def remove_lru(self):
        self.remove(self.tail.next)
    
    def add_recent(self, node):
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev = node
        node.prev.next = node
        self.node_map[node.key] = node

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.remove(node)
            self.add_recent(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.node_map) == self.capacity and key not in self.node_map:
            self.remove_lru()
        if key in self.node_map:
            self.remove(self.node_map[key])
        node = DoublyLinkedNode()
        node.key = key
        node.value = value
        self.add_recent(node)
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)