class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxP = 0

        l = 0 # buy - lowest price
        r = 1 # sell - higher price
        while r < len(prices):

            if prices[r] > prices[l]:
                # make a profit so update max

                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            
            else:
                # selling price is lower so move to be buying price
                l = r

            r += 1

        return maxP