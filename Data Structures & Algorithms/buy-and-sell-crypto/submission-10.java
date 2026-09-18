class Solution {

    public int maxProfit(int[] prices) {
        int l = 0, r = 1; // l = buy, r = sell
        int maxProfit = 0;

        while(r < prices.length) {
            if(prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                if(profit > maxProfit) {
                    maxProfit = profit;
                }
            } else {
                l = r;
            }
            r++;
        }
        return maxProfit;

    }
}
