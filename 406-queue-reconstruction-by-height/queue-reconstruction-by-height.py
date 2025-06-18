class SegmentTree:
    def __init__(self, n):
        self.sums = [0 for i in range(n)] + [1 for i in range(n)]
        self.n = n
        for i in range(n -1, 0, -1):
            self.sums[i] = self.sums[i*2] + self.sums[i*2+1]
    
    def update(self, i):
        i += self.n
        while i > 0:
            self.sums[i] -= 1
            i //= 2
    def get_range_sum(self, i, j):
        i += self.n
        j += self.n
        curr_sum = 0
        while i <= j and i != 0:
            # when i is on the right side
            if i % 2 == 1:
                curr_sum += self.sums[i]
                i += 1
            if j % 2 == 0:
                curr_sum += self.sums[j]
                j -= 1
            i //=2
            j //=2
        
        return curr_sum

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
        people.sort(key=lambda person: (person[0], -person[1]))
        segment_tree = SegmentTree(len(people))
        #print(segment_tree.sums)
        answer = [-1 for i in range(len(people))]
        for i in range(len(people)):
            h, k = people[i]
            #print("h,k:", h, k)
            spot = self.find_spot(segment_tree, k)
            answer[spot] = people[i]
            segment_tree.update(spot)
            #print(answer)
        return answer
            # you want to pick up the location that is bigger than k
            # it must be closest to k as much as possible


    def find_spot(self,segment_tree, k):
        l = 0
        r = segment_tree.n - 1
        i = None
        while l <= r:
            m = (l + r) // 2
            # the number of vacancy
            # because everything after this is bigger than you
            # you want to choose closest i to k but bigger than k
            curr_sum = segment_tree.get_range_sum(0, m)
            if segment_tree.get_range_sum(0, m) <= k:
                l = m + 1
            else:
                i = m
                r = m - 1
        return i 