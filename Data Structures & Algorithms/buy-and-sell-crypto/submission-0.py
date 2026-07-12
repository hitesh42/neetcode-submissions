class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        # sell 
        for p in prices:
            if p < buy:
                buy = p
            elif p-buy > profit:
                profit = p-buy
        return profit
        