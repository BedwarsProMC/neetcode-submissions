class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy low 
        r = 1 # sell high

        maxProfit = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            if buy < sell:
                profit = sell - buy
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit