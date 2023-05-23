class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.max_operation = max(len(word1), len(word2))
        return self.recursion(word1, word2, 0)

    def recursion(self, word1, word2, operation_count):
        if word1 == word2:
            return operation_count
        elif operation_count == self.max_operation:
            return float("inf")
        #どっちも0の時は上のif文で回収される。
        elif len(word1) == 0:
            return self.insert(word1, word2, operation_count)
        elif len(word2) == 0:
            return self.drop(word1, word2, operation_count)
        elif word1[0] == word2[0]:
            return self.recursion(word1[1:], word2[1:], operation_count)
        else:
            count_insert = self.insert(word1, word2, operation_count)
            count_drop = self.drop(word1, word2, operation_count)
            count_replace = self.replace(word1, word2, operation_count)
            return min([count_insert, count_drop, count_replace])

    def insert(self, word1, word2, operation_count):
        word1 = word2[0] + word1
        return self.recursion(word1, word2, operation_count+1)

    def drop(self, word1, word2, operation_count):
        word1 = word1[1:]
        return self.recursion(word1, word2, operation_count+1)

    def replace(self, word1, word2, operation_count):
        word1 = word2[0] + word1[1:]
        return self.recursion(word1, word2, operation_count+1)