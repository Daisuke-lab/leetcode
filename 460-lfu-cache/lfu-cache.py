class DoublyLinkedNode:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.count = 1
        
class LFUCache:

    def __init__(self, capacity: int):
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.count = -1
        self.head.count = float("inf")
        self.key_map = {}
        self.count_map = {}
        self.capacity = capacity
    
    def is_empty(self):
        return self.head.prev == self.tail and self.tail.next == self.head

    def get_min_count(self):
        if self.is_empty():
            return float("inf")
        else:
            return self.tail.next.count
    def get_max_count(self):
        if self.is_empty():
            return 0
        else:
            return self.head.prev.count

    def print_list(self):
        head = self.tail.next
        while head != self.head:
            self.print_node(head)
            head = head.next
    def print_node(self, node, debug=False):
        if debug:
            print("##############")
        print(f"FREQ:{node.count}, KEY:{node.key}, VAL: {node.value}")
        if debug:
            print("##############")

    def remove(self, key):
        node = self.key_map[key]
        tail = None
        head = None
        # when curr node is the only node for this count
        if node.prev.count != node.count and node.next.count != node.count:
            del self.count_map[node.count]
            tail = node.prev
            head = node.next
        else:
            if self.count_map[node.count] == node:
                self.count_map[node.count] = node.prev
        del self.key_map[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        if tail is None:
            tail = self.count_map[node.count]
            head = tail.next
        return tail, head

    def insert(self, node, tail=None, head=None):
        self.key_map[node.key] = node
        if node.count in self.count_map:
            head = self.count_map[node.count].next
            tail = self.count_map[node.count]
        else:
            # what if frequency (3,4) exists, and you are inserting 1
            # you don't know where to connect. Not like LRU cache, you can not choose head.prev as insertion point
            # you want to maintain each frequent tail and head
            if node.count < self.get_min_count():
                tail = self.tail
                head = self.tail.next
            elif node.count > self.get_max_count():
                tail = self.head.prev
                head = self.head
            #else:
                #print("you are here")
                # self.print_node(tail, True)
                # self.print_node(tail.next, True)
        node.next = head
        node.prev = tail
        head.prev = node
        tail.next = node
        self.count_map[node.count] = node

    def get(self, key: int) -> int:
        #print("GET::", key)
        result = -1
        if key in self.key_map:
            node = self.key_map[key]
            tail, head = self.remove(key)
            node.count += 1
            self.insert(node, tail, head)
            result = node.value
        #self.print_list()
        return result

    def put(self, key: int, value: int) -> None:
        #print("PUT::", key, value)
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            tail, head = self.remove(key)
            node.count += 1
            self.insert(node, tail, head)
        else:
            if len(self.key_map) == self.capacity:
                self.remove(self.tail.next.key)
            node = DoublyLinkedNode(key, value)
            self.insert(node)
        #self.print_list()
            
            



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)