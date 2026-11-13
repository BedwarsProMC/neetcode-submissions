class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        res = dp[amount]
        if res == amount + 1:
            return -1
        return res

        # memo = {} # rem -> min coins from this rem to reach 0

        # def dfs(rem):
        #     if rem == 0:
        #         return 0
        #     if rem < 0:
        #         return float('inf')
            
        #     if rem in memo:
        #         return memo[rem]

        #     best = float('inf')
        #     for c in coins:
        #         best = min(best, dfs(rem - c))
            
        #     memo[rem] = 1 + best
        #     return memo[rem]

        # res = dfs(amount)
        # if res == float('inf'):
        #     return -1
        # return res
        