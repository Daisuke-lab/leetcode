from itertools import combinations
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.MOD = 10 ** 9 + 7
        #return self.brute_force(n, minProfit, group, profit)
        self.memo = {}
        #self.memo = dp=[[[-1 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(len(group)+1)]
        return self.brute_force(n, minProfit, group, profit) % self.MOD
    
    def brute_force(self, n, minProfit, group, profit):
        count = 0
        indexes = [i for i in range(len(profit))]
        for i in range(len(indexes) + 1):
            #これはすべての組み合わせを取得するmethod
            #i=1の時は(1),(2) i=2の時は(1, 2), (2, 1)など
            index_combinations = combinations(indexes, i)
            for index_combination in index_combinations:
                _sum = sum([profit[index] for index in index_combination])
                cost = sum([group[index] for index in index_combination])
                if _sum >= minProfit and cost <=n:
                    count += 1

        return count