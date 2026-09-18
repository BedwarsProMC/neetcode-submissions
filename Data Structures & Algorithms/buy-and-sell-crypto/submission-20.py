class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2): return 0

        maxP = 0

        l = 0
        r = 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(maxP, profit)
            else: 
                l = r
            r += 1

        return maxP