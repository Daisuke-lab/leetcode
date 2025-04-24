class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        
        sPre = [0] * n
        for i in range(1, n):
            sPre[i] = sPre[i - 1] + skill[i]

        tSum = skill[0] * mana[0]

        for j in range(1, m):
            tMax = skill[0] * mana[j]
            for i in range(1, n):
                tDiff = sPre[i] * mana[j - 1] - sPre[i - 1] * mana[j]
                if tDiff > tMax:
                    tMax = tDiff
            tSum += tMax

        return tSum + sPre[n - 1] * mana[m - 1]