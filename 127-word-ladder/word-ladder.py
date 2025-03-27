class Solution:
    # It can be DP, you change each letter to reach the endWord
    # you can return the number of changes
    # you also want to maintain visited (set) to avoid going back to the original string
    # you can think of this as graph (if only one character is different, it's adjacent)
    # dijkstra algorrithm
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        self.dj_map = self.init_dj_map(beginWord, endWord, wordList)
        self.ad_list = self.init_ad_list(beginWord, endWord, wordList)
        #print(self.ad_list)
        visited = set()
        waiting_heap = []
        word = beginWord
        while word:
            visited.add(word)
            for ad_word in self.ad_list[word]:
                distance = self.dj_map[word]["distance"] + 1
                if distance < self.dj_map[ad_word]["distance"]:
                    self.dj_map[ad_word]["distance"] = distance
                    self.dj_map[ad_word]["prev"] = word
                if ad_word not in visited:
                    heapq.heappush(waiting_heap, (distance, ad_word))

            word = heapq.heappop(waiting_heap)[1] if waiting_heap else None
        
        if self.dj_map[endWord]["distance"] == float("inf"):
             self.dj_map[endWord]["distance"] = 0
        return self.dj_map[endWord]["distance"]



    def init_ad_list(self, beginWord, endWord, wordList):
        ad_list = {}
        chars = "abcdefghijklmnopqrstuvwxyz"
        allWords = {beginWord, endWord}
        allWords = wordList | allWords
        for word in allWords:
            ad_list[word] = ad_list.get(word, set())
            for i in range(len(word)):
                for c in chars:
                    ad_word = word[:i] + c + word[i+1:]
                    if ad_word in allWords and ad_word != word:
                        ad_list[word].add(ad_word)
        return ad_list
                    

    def init_dj_map(self, beginWord, endWord, wordList):
        dj_map = {}
        allWords = {beginWord, endWord}
        allWords = wordList | allWords
        for word in allWords:
            dj_map[word] = {"distance": float("inf"), "prev": None}
        dj_map[beginWord]["distance"] = 1
        return dj_map