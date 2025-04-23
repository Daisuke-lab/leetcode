class SegmentTree:
    def __init__(self, N):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.build(N)

    def build(self, N):
        self.tree = [0] * (2 * self.n)
        for i in range(N):
            self.tree[self.n + i] = 1
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, i, val):
        self.tree[self.n + i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            self.tree[j] = self.tree[j << 1] + self.tree[j << 1 | 1]
            j >>= 1

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res

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
                cnt = segTree.query(0, mid)
                if cnt > p[1]:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
                    
            res[idx] = p
            segTree.update(idx, 0)
            
        return res