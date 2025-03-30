class Trie:
    def __init__(self):
        self.next = {}
        self.is_end = False


class Solution:
    # Same word can be used multiple times
    # shift s until you find the word
    # if you find word, reduce string and dp
    # self.memo = {word: True}
    # I want to make trie
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.root = self.build_trie(wordDict)
        self.memo = {}
        return self.dp(s)

    def dp(self, s):
        head = self.root
        if s == "":
            return False
        if s in self.memo:
            return self.memo[s]
        result = False
        for i in range(len(s)):
            c = s[i]
            if c not in head.next:
                break
            head = head.next[c]
            if head.is_end:
                result = self.dp(s[i+1:]) if i + 1 < len(s) else True
                if result:
                    break
        self.memo[s] = result
        return result

    def build_trie(self, words):
        root = head = Trie()
        for word in words:
            head = root
            for i,c in enumerate(word):
                if c not in head.next:
                    head.next[c] = Trie()
                head = head.next[c]
                if i == len(word) -1:
                    head.is_end = True
        return root




        