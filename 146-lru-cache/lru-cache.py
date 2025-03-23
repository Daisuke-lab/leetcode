class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # you want map {count: key}
    # but count can be increased
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.least_dummy = Node(0, 0)
        self.latest_dummy = Node(0, 0)
        self.least_dummy.next = self.latest_dummy
        self.latest_dummy.prev = self.least_dummy

    def insert(self, node):
        prev_latest_node = self.latest_dummy.prev
        self.latest_dummy.prev = node
        node.next = self.latest_dummy
        node.prev = prev_latest_node
        prev_latest_node.next = node


    def remove(self, node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
        del self.cache[node.key]



    def get(self, key: int) -> int:
        #print(f"GET:: key={key}, cache={self.cache}")
        if key not in self.cache:
            return - 1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        self.cache[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        #print(f"PUT:: key={key}, value={value}, cache={self.cache}")
        if self.capacity == len(self.cache) and key not in self.cache:
            self.remove(self.least_dummy.next)
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)