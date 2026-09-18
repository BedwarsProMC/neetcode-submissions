class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        maxP = 0

        l = 0
        r = 1

        while r < len(prices):
            
                # r += 1

            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

            if prices[r] < prices[l]:
                l = r
            # else:


            r += 1

        return maxP