class Solution:
    # i is current index
    # j is a splitter
    
    def integerBreak(self, n: int) -> int:
        tab = [i for i in range(n+1)]
        tab[n] = 0
        for i in range(n+1):
            for j in range(i):
                left = j
                right = i - j
                product = tab[left] * tab[right]
                tab[i] = max(tab[i], product)
        return tab[n]