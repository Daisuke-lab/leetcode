class DoublyLinkedList:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.prev = self.tail
        self.tail.next = self.head 
        self.capacity = capacity
        self.node_map = {}

    def delete(self, node):
        if node in [self.head, self.tail]:
            return
        del self.node_map[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        self.node_map[node.key] = node
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.delete(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = DoublyLinkedList(key, value)
        if key in self.node_map:
            self.delete(self.node_map[key])
        if self.capacity == len(self.node_map):
            self.delete(self.tail.next)
        self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)