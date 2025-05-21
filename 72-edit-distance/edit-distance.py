class Solution:
    # case 1: replace current char to match word2 => and DP shrunk word2
    # case 2: remove current char => DP *original word2
    # case 3: insert exact char => DP *shrunk word2

    # you can cache, (word1, word2) as memo *you can not use i and j due to insertion and removal
    # m*n
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[
            float("inf") for i in range(len(word2)+1)]
            for j in range(len(word1)+1)]
        memo[0][0] = 0
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0 and j == 0:
                    memo[i][j] = 0
                elif i == 0:
                    memo[i][j] = j
                elif j == 0:
                    memo[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = min(memo[i-1][j-1], memo[i-1][j], memo[i][j-1]) + 1
        return memo[-1][-1]