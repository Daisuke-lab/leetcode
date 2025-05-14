inf = float('inf')
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        vi = sorted([(v, i) for i, v in enumerate(nums)])
        n2i = {t[1]: i for i, t in enumerate(vi)}
        vals = [t[0] for t in vi]

        h = len(bin(n)[2:]) + 1
        jumps = [[-1] * h for _ in range(n)]
        j = 0
        for i in range(n):
            while j+1 < n and vals[j+1] - vals[i] <= maxDiff:
                j += 1
            jumps[i][0] = j
        for j in range(1, h):
            for i in range(n):
                jumps[i][j] = jumps[jumps[i][j-1]][j-1]
        
        def query(a, b, h):
            if a == b:
                return 0
            if jumps[a][0] >= b:
                return 1
            if jumps[a][h] < b:
                return inf 
            for j in range(h, -1, -1):
                if jumps[a][j] < b:
                    break
            return (1 << j) + query(jumps[a][j], b, j)
            
        
        res = []
        for a, b in queries:
            a, b = n2i[a], n2i[b]
            cur = query(min(a, b), max(a, b), h-1)
            res.append(cur if cur < inf else -1)
        return res