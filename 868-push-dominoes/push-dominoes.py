class Solution:
    # Brute Force
    # take 1 step in each n iteration
    # in the worst case you have to put down n times
    # O(n^2)

    # Or you can use BFS
    # 1. collect L and R
    # 2. put it down (check if left side is also going down)
    def pushDominoes(self, dominoes: str) -> str:
        L_fallings = set()
        R_fallings = set()
        for i in range(0, len(dominoes)):
            if dominoes[i] == "L":
                L_fallings.add(i)
            if dominoes[i] == "R":
                R_fallings.add(i)
        while L_fallings or R_fallings:
            new_L_fallings = set()
            new_R_fallings = set()
            for i in L_fallings:
                if dominoes[i] == "L" and i > 0 and dominoes[i-1] == "." and i-2 not in R_fallings:
                    dominoes = dominoes[:i-1] + "L" + dominoes[i:] 
                    new_L_fallings.add(i-1)
            for i in R_fallings:
                if dominoes[i] == "R" and i+1 < len(dominoes) and dominoes[i+1] == "." and i + 2 not in L_fallings:
                    #dominoes[i+1] = "R"
                    dominoes = dominoes[:i+1] + "R" + dominoes[i+2:]
                    new_R_fallings.add(i+1)
            L_fallings = new_L_fallings
            R_fallings = new_R_fallings
        return dominoes 
                
        