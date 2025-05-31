class DoublyLinkedList:
    def __init__(self, value=None, index=None):
        self.index = index
        self.value = value
        self.prev = None
        self.next = None

    def __lt__(self, other):
        return self.value < other.value

class Solution:
    # get the min sum => heap
    # confirm it's ascending => doubly linked list?
    # count the violation first. when you merge it, you can check how many violations are resolved
    # case 1: i > j (when you merge i and j)
    # case 2: i -1 > i 
    # case 3: j + 1 < j
    # you might create a new violation

    # base case: violation is 0
    # min_heap (sum, node1, node2)
    # if node1 and node2 are not linked anymore, discard it 
    # 
    def minimumPairRemoval(self, nums: List[int]) -> int:
        violations, min_heap = self.init_linked_list(nums)
        # print(violations)
        # print(min_heap)
        operations = 0
        while min_heap:
            
            if violations == 0:
                return operations
            # self.print_list()
            # print(violations)
            ad_sum, index, prev, curr = heapq.heappop(min_heap)
            if not self.is_adjacent(prev, curr):
                continue
            left_violated, mid_violated, right_violated = self.check_violation(prev, curr)
            merged_node = self.merge(prev, curr)
            operations += 1
            left_resolved, right_resolved = self.check_resolution(merged_node)
            if mid_violated:
                violations -= 1
            if left_violated and left_resolved:
                violations -= 1
            if right_violated and right_resolved:
                violations -= 1
            if not left_violated and not left_resolved:
                violations += 1
            if not right_violated and not right_resolved:
                violations += 1
            self.add_new_pair(merged_node, min_heap)
             
        return operations

    def print_list(self):
        curr = self.tail.next
        while curr.value is not None:
            print(curr.value, end=" ")
            curr = curr.next
        print("")
    def add_new_pair(self, node, min_heap):
        if node.prev.value is not None:
            left_sum = node.prev.value + node.value
            heapq.heappush(min_heap, (left_sum, node.prev.index, node.prev, node))
        if node.next.value is not None:        
            right_sum = node.next.value + node.value   
            heapq.heappush(min_heap, (right_sum, node.index, node, node.next))

    def merge(self, node1, node2):
        merged_node = DoublyLinkedList(node1.value + node2.value, node1.index)
        merged_node.prev = node1.prev
        merged_node.next = node2.next
        node1.prev.next = merged_node
        node2.next.prev = merged_node
        return merged_node

    def is_adjacent(self, node1, node2):
        return node1.next == node2 and node2.prev == node1

    def check_violation(self, node1, node2):
        left_violated = False
        mid_violated = False
        right_violated = False
        if node1.prev.value is not None and node1.prev.value > node1.value:
            left_violated = True
        if node1.value > node2.value:
            mid_violated = True
        if node2.next.value is not None and node2.next.value < node2.value:
            right_violated = True
        return left_violated, mid_violated, right_violated

    def check_resolution(self, node):
        left_resolved = False
        right_resolved = False
        if node.prev.value is None or node.prev.value <= node.value:
            left_resolved = True
        if node.next.value is None or  node.next.value >= node.value:
            right_resolved = True
        return left_resolved, right_resolved
        

    def init_linked_list(self, nums):
        violations = 0
        min_heap = []
        tail = DoublyLinkedList()
        head = DoublyLinkedList()
        prev = tail
        for i in range(len(nums)):
            
            node = DoublyLinkedList(nums[i], i)
            self.insert(prev, head, node)
            if i != 0:
                ad_sum = nums[i] + nums[i-1]
                min_heap.append((ad_sum, i-1, prev, node))
                if nums[i] < nums[i-1]:
                    violations += 1
            prev = node
        heapq.heapify(min_heap)
        self.head = head
        self.tail = tail
        return violations, min_heap

    def insert(self, prev, head, node):
        node.prev = prev
        node.next = head
        prev.next = node
        head.prev = node

        