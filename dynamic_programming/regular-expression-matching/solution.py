class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        #indexにより後ろから見ていくという発想がなかった。かけていた発想はこれだけ。
        #2個同時に見ていかないといけないという発想はあっていた。
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, memo, s, p, i, j):
        key = (i, j)
        if key in memo:
            return memo[key]

        #indexが0以下のケース。sもpも0
        if i == -1 and j == -1:
            memo[key] = True
            return True

        #sがだけが残っているケース。
        if i != -1 and j == -1:
            memo[key] = False
            return memo[key]

        #s = ""で、p=*のケース
        if i == -1 and p[j] == '*':
            k = j
            #二個前の繰り返さなくていいやつを持ってくる。
            while k != -1 and p[k] == '*':
                k -= 2
            
            #それが見つからない場合、s=""でokなのでTrue
            if k == -1:
                memo[key] = True
                return memo[key]
            #それ以外はfalse
            memo[key] = False
            return memo[key]
        
        #s = ""で p!="*"の時はアウト
        if i == -1 and p[j] != '*':
            memo[key] = False
            return memo[key]

        
        if p[j] == '*':
            #pを二個前に戻して比較している。.*やa*の繰り返しが0の時を想定
            if self.backtrack(memo, s, p, i, j - 2):
                memo[key] = True
                return memo[key]
            #.*やa*の時、一旦sを一文字減らして、recursion
            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(memo, s, p, i - 1, j):
                    memo[key] = True
                    return memo[key]
        
        #pが.かaの時、sとpどっちも一文字減らしてrecurion
        #.*やa*のケースは上のifで巻き取られているのでok
        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(memo, s, p, i - 1, j - 1):
                memo[key] = True
                return memo[key]

        memo[key] = False
        return memo[key]

                
            