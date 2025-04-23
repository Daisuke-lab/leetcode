class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [1] * (2 * self.n)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, val):
        i += self.n
        diff = val - self.tree[i]
        self.tree[i] = val
        i //= 2
        while i > 0:
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
            i //= 2

    def sumRange(self, i, j):
        answer = 0
        i += self.n
        j += self.n
        while i <= j:
            if i % 2 == 1:
                answer += self.tree[i]
                i += 1
            if j % 2 == 0:
                answer += self.tree[j]
                j -= 1
            i //= 2
            j //= 2
        return answer

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        # small heights and big k
        people.sort(key=lambda x: (x[0], -x[1]))
        print(people)
        res = [[] for _ in range(n)]

        segTree = SegmentTree(n)
        for height, k in people:
            l, r = 0, n - 1
            i = 0
            while l <= r:
                m = (l + r) // 2
                # when you still have space and you want to put right most position
                # afterward, you keep putting bigger value, so position of person fixed 100%
                if segTree.sumRange(0, m) > k:
                    i = m
                    r = m - 1
                else:
                    l = m + 1
                    
            res[i] = [height, k]
            segTree.update(i, 0)
            
        return res