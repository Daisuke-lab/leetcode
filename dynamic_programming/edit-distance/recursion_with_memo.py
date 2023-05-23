class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.max_operation = max(len(word1), len(word2))
        return self.recursion_with_memo(word1, word2, {})

    def recursion_with_memo(self, word1, word2, memo):
        key = (word1, word2)
        if word1 == word2:
            return 0
        elif key in memo:
            return memo[key]
        #どっちも0の時は上のif文で回収される。
        elif len(word1) == 0:
            memo[key] = self.insert(word1, word2, memo)
            return memo[key]
        elif len(word2) == 0:
            memo[key] = self.drop(word1, word2, memo)
            return memo[key]
        elif word1[0] == word2[0]:
            memo[key] =  self.recursion_with_memo(word1[1:], word2[1:], memo)
            return memo[key]
        else:
            count_insert = self.insert(word1, word2, memo)
            count_drop = self.drop(word1, word2, memo)
            count_replace = self.replace(word1, word2, memo)
            memo[key] = min([count_insert, count_drop, count_replace])
            return memo[key]

    def insert(self, word1, word2, memo):
        word1 = word2[0] + word1
        count = self.recursion_with_memo(word1, word2, memo)
        count += 1
        if count >  self.max_operation:
            return float("inf")
        return count

    def drop(self, word1, word2, memo):
        word1 = word1[1:]
        count = self.recursion_with_memo(word1, word2, memo)
        count += 1
        if count >  self.max_operation:
            return float("inf")
        return count

    def replace(self, word1, word2, memo):
        word1 = word2[0] + word1[1:]
        count =  self.recursion_with_memo(word1, word2, memo)
        count += 1
        if count >  self.max_operation:
            return float("inf")
        return count