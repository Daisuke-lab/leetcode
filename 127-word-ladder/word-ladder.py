class Solution:
    # It can be DP, you change each letter to reach the endWord
    # you can return the number of changes
    # you also want to maintain visited (set) to avoid going back to the original string
    # you can think of this as graph (if only one character is different, it's adjacent)
    # dijkstra algorrithm
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        words = set(wordList)
        words.add(beginWord)
        ad_list = self.init_ad_list(words)
        queue = collections.deque()
        queue.append(beginWord)
        visited = set()
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                #print(word)
                visited.add(word)
                if word == endWord:
                    return count
                for i in range(len(word)):
                    pattern = f"{word[:i]}*{word[i+1:]}"
                    for ad in ad_list[pattern]:
                        if ad not in visited:
                            queue.append(ad)
        return 0


        
    def init_ad_list(self, words):
        ad_list = defaultdict(set)
        for word in words:
            for j in range(len(word)):
                pattern = f"{word[:j]}*{word[j+1:]}"
                ad_list[pattern].add(word)
        return ad_list
        
