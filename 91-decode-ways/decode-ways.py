class Solution:
    def numDecodings(self, s: str) -> int:
        tab = [0 for i in range(len(s))]
        tab[0] = 1 if s[0] != "0" else 0
        if len(s) == 1:
            return tab[0]
        if int(s[0]) == 1 and int(s[1]) in [0,1,2,3,4,5,6,7,8,9]:
            tab[1] += 1
        if int(s[0]) == 2 and int(s[1]) in [0,1,2,3,4,5,6]:
            tab[1] += 1
        if int(s[0]) != 0 and int(s[1]) != 0:
            tab[1] += 1
        for i in range(2, len(s)):
            if int(s[i]) != 0:
                tab[i] += tab[i-1]
            if int(s[i-1]) == 1 and int(s[i]) in [0,1,2,3,4,5,6,7,8,9]:
                tab[i] += tab[i-2]
            if int(s[i-1]) == 2 and int(s[i]) in [0,1,2,3,4,5,6]:
                tab[i] += tab[i-2]
        print(tab)
        return tab[-1]

        