
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.MOD = 10 ** 9 + 7
        self.memo = dp=[[[-1 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(len(group)+1)]
        return self.dynamic_with_memo(n, minProfit, group, profit, len(group) -1, len(group)) % self.MOD
    
    def dynamic_with_memo(self, budget, minProfit, group, profit, size):
        if budget < 0:
            return 0
        if budget == 0:
            if minProfit == 0:
                return 1
            else:
                return 0
        if size == 0:
            if minProfit == 0:
                return 1
            else:
                return 0
        if self.memo[size][budget][minProfit] != -1:
            return self.memo[size][budget][minProfit]
        
        count_without_item = self.dynamic_with_memo2(budget, minProfit, group, profit, size-1)
        
        if group[size-1] <= budget:
            count_with_item = self.dynamic_with_memo2(budget-group[size-1], max(0, minProfit-profit[size-1]), group, profit, size-1)
        else:
            count_with_item = 0

        count = (count_with_item + count_without_item)
        
        self.memo[size][budget][minProfit] = count
        return self.memo[size][budget][minProfit]