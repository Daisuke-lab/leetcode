class DoublyLinkedList:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = 1

    def is_only_node_with_freq(self):
        if self.next and self.next.freq == self.freq:
            return False
        if self.prev and self.prev.freq == self.freq:
            return False
        return True

    def is_head_of_freq(self):
        if self.next and self.next.freq == self.freq:
            return False
        return True


class LFUCache:
    # key_map is useful? => YES for get 
    # freq_map: you keep the head of the frequency
    
    # delete the least frequent
    # tail.next
    
    # delete any node
    # if it is only node for the frequcny, delete frequency key
    # if it is the head of the frequency, change the head
    
    # insert (update frequency)
    # how to get the next frequency?? => check the past frequency head.next
    # if it is bigger than new frequency, that should be your next
    # if it is the same with new frequenct, that should be your prev

    # insert (new node)
    # if the freq 1 exists, just insert it as a head
    # if the freq 1 doesn't exist, tail.next would be your next and tial is prev
    def __init__(self, capacity: int):
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.head.freq = float("inf")
        self.tail.freq = - float("inf")
        self.head.prev = self.tail
        self.tail.next = self.head
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = {}

    def delete(self, node):
        if node in [self.head, self.tail]:
            return
        # if node.key not in self.key_map:
        #     return 
        if node.is_only_node_with_freq():
            del self.freq_map[node.freq]
        elif node.is_head_of_freq():
            self.freq_map[node.freq] = node.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.key_map[node.key]

    def insert(self, node):
        if 1 in self.freq_map:
            head = self.freq_map[1].next
            tail = head.prev
        else:
            head = self.tail.next
            tail = self.tail
        node.prev = tail
        node.next = head
        tail.next = node
        head.prev = node
        self.key_map[node.key] = node
        self.freq_map[1] = node

    def update(self, node):
        if node.is_only_node_with_freq():
            tail = node.prev
            head = node.next
        self.delete(node)
        node.freq += 1
        if node.freq in self.freq_map:
            tail = self.freq_map[node.freq]
            head = tail.next
        elif node.freq - 1 in self.freq_map:
            tail = self.freq_map[node.freq -1]
            head = tail.next
        node.prev = tail
        node.next = head
        tail.next = node
        head.prev = node
        self.freq_map[node.freq] = node
        self.key_map[node.key] = node
        


    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.update(node)    
        else:
            if self.capacity == len(self.key_map):
                self.delete(self.tail.next)
            node = DoublyLinkedList(key, value)
            self.insert(node)




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)