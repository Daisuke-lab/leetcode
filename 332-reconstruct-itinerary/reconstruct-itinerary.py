class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.ad_list = self.init_ad_list(tickets)

        # You don't have to calculate for start vertex in this question
        start_v = "JFK"
        self.answer = []
        self.dfs(start_v)
        return self.answer[::-1]

    def dfs(self, src):
        while self.ad_list[src]:
            dest = self.ad_list[src].pop()
            self.dfs(dest)
        self.answer.append(src)

    def init_ad_list(self, edges):
        edges.sort(reverse=True)
        ad_list = defaultdict(list)
        for src, dest in edges:
            ad_list[src].append(dest)
        return ad_list