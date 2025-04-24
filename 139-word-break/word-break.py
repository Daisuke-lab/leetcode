


class Solution:
    # memo [i] = true/false
    # 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.tab = [None for i in range(len(s))]
        self.words = set(wordDict)
        self.s = s
        return self.dp(0)


    def dp(self, i):
        if i == len(self.s):
            return True
        if self.tab[i] != None:
            return self.tab[i]
        result = False
        for j in range(i, len(self.s)):
            subs = self.s[i:j+1]
            if subs in self.words and self.dp(j+1):
                result = True
                break
        self.tab[i] = result
        return result

        