


class Solution:
    # Same word can be used multiple times
    # shift s until you find the word
    # if you find word, reduce string and dp
    # self.memo = {word: True}
    # I want to make trie
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tab = [False for i in range(len(s) + 1)]
        tab[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                curr_length = len(s) - i + 1
                curr_word = s[i:i+len(word)]
                if curr_length < len(word):
                    continue
                if curr_word == word:
                    tab[i] = tab[i + len(word)]
                if tab[i]:
                    break
        return tab[0]
                




        