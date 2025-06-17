class LinkedNode():
    def __init__(self, i=None):
        self.i = i
        self.next = None

class Solution:
    # Brute Force
    # Try every combination n!
    
    # start from higher height
    # 1. sort by k
    # 2. starts from the top, and then insert when you have k nodes before you
    
    # start from shorter height
    # adding bigger number behind it, doesn't affect the rule
    # =>  but sometimes you want to add in-between
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        head = LinkedNode()
        tail = LinkedNode()
        tail.next = head
        people.sort(key=lambda person: (-person[0], person[1]))
        #print(people)
        for i in range(len(people)):
            h, k = people[i]
            curr = tail
            node = LinkedNode(i)
            while k != 0:
                curr = curr.next
                k -= 1
            #print(i)
            node.next = curr.next
            curr.next = node
        answer = []
        curr = tail.next
        while curr != head:
            answer.append(people[curr.i])
            curr = curr.next
        return answer