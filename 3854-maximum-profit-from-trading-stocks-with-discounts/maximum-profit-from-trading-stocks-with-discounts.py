INF = -10**18
class Solution:
    # sounds like dp + grpah
    # create graph
    # it all connected directed graph without cycle
    # what is args? buget, curr, boss_bought
    # return max profit

    # currently calculating the max profit path
    # how do you split the budget? how do you parition?
    # split buget 100 to 5 is hell. you wouldn't want to do that
    # you want to make it 1 line
    # topological sort ? 
    # you want to know parent purchased or not. which is now hard by topological sort
    # number is too big for bitmask dp

    # it sounds like knapsack dp but discount makes this problem tricky
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        self.present = present
        self.future = future
        self.ad_list = self.init_ad_list(n, hierarchy)
        self.budget = budget
        return max(self.dfs(1)[0])
        

    def dfs(self, curr):
        full_price = self.present[curr-1]
        half_price = full_price // 2
        profit_without_discount = self.future[curr-1] - full_price
        profit_with_discount = self.future[curr-1] - half_price

        # he maximum profit at u when boss doesn't buy and u don't buy with budget i
        skip_skip = [0] + [INF] * self.budget
        # The maximum profit at u when boss doesn't buy and u buy with budget i
        skip_buy = [INF] * (self.budget+1)
        # The maximum profit at u when boss buys and u don't buy with budget i
        buy_skip = [0] + [INF] * self.budget
        # The maximum profit at u when boss buys and u buy with budget i
        buy_buy  = [INF] * (self.budget+1)
        
        if full_price <= self.budget:
            skip_buy[full_price] = profit_without_discount
        if half_price <= self.budget:
            buy_buy[half_price] = profit_with_discount

        for ad in self.ad_list[curr]:
            # you calculate the max profit in all budgets when curr buy and doesn't buy
            curr_skip_dp, curr_buy_dp = self.dfs(ad)
            # 
            skip_skip = self.merge(skip_skip, curr_skip_dp)
            skip_buy = self.merge(skip_buy, curr_buy_dp)
            buy_skip = self.merge(buy_skip, curr_skip_dp)
            buy_buy = self.merge(buy_buy, curr_buy_dp)
        
        parent_skip_dp = [max(skip_skip[i], skip_buy[i]) for i in range(self.budget+1)]
        parent_buy_dp = [max(buy_skip[i], buy_buy[i]) for i in range(self.budget+1)]
        return parent_skip_dp, parent_buy_dp



    def merge(self, profits1, profits2):
        total_budget = len(profits1)
        profits = [INF] * total_budget
        for budget in range(total_budget):
            curr_profit = profits1[budget]
            # 
            if curr_profit == INF:
                continue
            remaining_budget = total_budget - budget
            for upcoming_budget in range(remaining_budget):
                upcoming_profit = profits2[upcoming_budget]
                if upcoming_profit == INF:
                    continue
                profits[budget +upcoming_budget] = max(profits[budget +upcoming_budget], curr_profit +upcoming_profit)
        return profits
            

        
    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(1, n+1)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
        return ad_list