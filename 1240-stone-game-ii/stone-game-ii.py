class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        self.memo = [[[
            -1 for p in range(2)]
            for q in range(len(piles)+1)]
            for i in range(len(piles))]
        return self.dp(0, 1, True)

    def dp(self, i, m, is_alice):
        
        if i >= len(self.piles):
            return 0

        if self.memo[i][m][is_alice] != -1:
            return self.memo[i][m][is_alice]
        
        result = 0
        if is_alice:
            current = 0
            for x in range(1, 2*m + 1):
                j = i + x -1
                if j >= len(self.piles): # j = i + x -1 < len(pile) -1 <=> i + x < len(piles) <=> m < len(piles) - x
                    break
                current += self.piles[j]
                result = max(result, self.dp(i+x, max(x, m), False) + current)
        else:
            result = float("inf")
            for x in range(1, 2*m + 1):
                result = min(result, self.dp(i+x, max(x, m), True))
        self.memo[i][m][is_alice] = result
        #print(f"i:{i}, m:{m}, is_alice:{is_alice}, result:{result}")
        return result
                


        

        