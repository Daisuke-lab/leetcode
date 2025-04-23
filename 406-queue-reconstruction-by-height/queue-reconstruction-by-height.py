class SegmentTree:
    def __init__(self, n):
        self.n = n
        # while (self.n & (self.n - 1)) != 0:
        #     self.n += 1
        self.build(n)

    def build(self, n):
        self.tree = [0] * (2 * self.n)
        for i in range(n):
            self.tree[self.n + i] = 1
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
        people.sort(key=lambda x: (x[0], -x[1]))
        res = [[] for _ in range(n)]

        segTree = SegmentTree(n)
        for p in people:
            l, r = 0, n - 1
            idx = 0
            while l <= r:
                mid = (l + r) >> 1
                cnt = segTree.sumRange(0, mid)
                if cnt > p[1]:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
                    
            res[idx] = p
            segTree.update(idx, 0)
            
        return res