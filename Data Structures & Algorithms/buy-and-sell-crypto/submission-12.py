class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        l = 0
        h = l + 1

        while h < len(prices):
            buy = prices[l]
            sell = prices[h]


            # always sell at a higher price
            
            if buy < sell:
                profit = sell - buy

                maxProfit = max(profit, maxProfit)
                h += 1

            else:
                l = h
                h = l + 1


        return maxProfit