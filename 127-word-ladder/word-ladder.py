class Solution:
    # h*t
    # create ad_list
    # dijkstra
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.words = wordList + [beginWord]
        self.ad_list = self.init_ad_list(self.words)
        queue = collections.deque()
        queue.append((1, beginWord))
        visited = set()
        while queue:
            count, word = queue.popleft()
            if word in visited:
                continue
            if word == endWord:
                return count
            visited.add(word)
            for i in range(len(word)):
                regex = word[:i] + "*" + word[i+1:]
                for ad in self.ad_list[regex]:
                    queue.append((count+1, ad))
        return 0


    def init_ad_list(self, words):
        ad_list = {}
        for word in words:
            for i in range(len(word)):
                regex = word[:i] + "*" + word[i+1:]
                ads = ad_list.get(regex, set())
                ads.add(word)
                ad_list[regex] = ads
        return ad_list