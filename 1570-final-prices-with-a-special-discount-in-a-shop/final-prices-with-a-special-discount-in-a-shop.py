class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts = {}
        stack = []
        for i in range(len(prices)):
            while stack and stack[-1][1] >= prices[i]:
                j, highest_price = stack.pop()
                discounts[j] = prices[i]
            stack.append((i, prices[i]))
        answer = []
        for i in range(len(prices)):
            answer.append(prices[i] - discounts.get(i, 0))
        return answer