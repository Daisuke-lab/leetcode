
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.MOD = 10 ** 9 + 7
        #return self.brute_force(n, minProfit, group, profit)
        self.memo = {}
        #self.memo = dp=[[[-1 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(len(group)+1)]
        return self.dynamic_with_memo(n, minProfit, group, profit, len(group) -1) % self.MOD
    
    def dynamic_with_memo(self, budget, minProfit, group, profit, index):
        key = f"budget{budget}_minProfit{minProfit}_index{index}"
        if budget < 0:
            return 0

        elif budget == 0:
            if minProfit == 0:
                return 1
            else:
                return 0

        if index < 0:
            if minProfit == 0:
                return 1
            else:
                return 0

        if self.memo.get(key): return self.memo.get(key)

        count_without_item = self.dynamic_with_memo(budget, minProfit, group, profit, index -1)

        if budget >= group[index]:
            count_with_item = self.dynamic_with_memo(budget - group[index], max(0, minProfit-profit[index]), group, profit, index - 1)
        else:
            count_with_item = 0
        self.memo[key] = count_with_item + count_without_item
        return self.memo[key]