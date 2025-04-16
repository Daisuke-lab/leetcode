class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        self.ad_list = self.init_ad_list(wordList)
        self.dj_map = self.init_dj_map(self.ad_list, beginWord)
        min_heap = [(1, beginWord)]
        visited = set()
        while min_heap:
            distance, word = heapq.heappop(min_heap)
            if word in visited:
                continue
            visited.add(word)
            for ad in self.ad_list[word]:
                if self.dj_map[ad] > 1 + distance:
                    self.dj_map[ad] = 1 + distance
                if ad not in visited:
                    heapq.heappush(min_heap, (distance + 1, ad))
        return self.dj_map[endWord] if self.dj_map[endWord] != float("inf") else 0

    def init_dj_map(self, ad_list, beginWord):
        # {node: distance}
        dj_map = {}
        for node in ad_list:
            dj_map[node] = float("inf")
        dj_map[beginWord] = 1
        return dj_map

    def init_ad_list(self, wordList):
        ad_list = {}
        words = set(wordList)
        for word in wordList:
            for i in range(len(word)):
                for c in "qwertyuiopasdfghjklzxcvbnm":
                    ad = f"{word[:i]}{c}{word[i+1:]}"
                    ads = ad_list.get(word, set())
                    if ad in words:
                        ads.add(ad)
                    ad_list[word] = ads
        return ad_list
                

        
