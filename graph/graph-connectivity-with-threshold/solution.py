# union findを知らないと解けない。
#　後は公約数の発想がpythonであるか。


class DSU:
	def __init__(self, n):
		self.par = list(range(n))
		self.rank = [1] * n
		self.size = 1
	
	def find(self, u):
		if u != self.par[u]:
			self.par[u] = self.find(self.par[u])
		return self.par[u]
	
	def union(self, u, v):
		uu, vv = self.find(u), self.find(v)
		if uu == vv:
			return False
		if self.rank[uu] > self.rank[vv]:
			self.par[vv] = uu
		elif self.rank[vv] > self.rank[uu]:
			self.par[uu] = vv
		else:
			self.par[uu] = vv
			self.rank[vv] += 1
		self.size += 1
		return True

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = DSU(n+1)
        for z in range(threshold+1, n+1):
            for x in range(z+z, n+1, z):
                uf.union(z, x)
        ans = [False] * len(queries)
        for i, (u, v) in enumerate(queries):
            ans[i] = uf.find(u) == uf.find(v)
        return ans