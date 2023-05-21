
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.MOD = 10 ** 9 + 7
        #return self.brute_force(n, minProfit, group, profit)
        self.memo = {}
        #self.memo = dp=[[[-1 for _ in range(minProfit+1)] for _ in range(n+1)] for _ in range(len(group)+1)]
        return self.recursion(n, minProfit, group, profit, []) % self.MOD
    

    def recursion(self, n, minProfit, group, profit, counts, visited):
        #下のiterationはPではなくcombination (C)で回しているので同じのが回収されないようにvisitedはskipする。
        if f"{group}_{profit}" in visited:
            return
        if minProfit <= 0 and n >= 0:
            visited.append(f"{group}_{profit}")
            #intでcountを管理すると、recursionで値がupdateされないのでlistで数を増やしていって、len(counts)でcountを取得する。
            counts.append(None)
        for i in range(len(profit)):
            #いきなりprofitからpopしてしまうと、二回目のloopの時にもその要素がなくなっている。
            new_profit = [_profit for _profit in profit]
            new_group = [cost for cost in group]
            _profit = new_profit.pop(i)
            cost = new_group.pop(i)
            new_minProfit = minProfit - _profit
            new_n = n - cost
            self.recursion(new_n, new_minProfit, new_group, new_profit, counts, visited)
        return len(counts)