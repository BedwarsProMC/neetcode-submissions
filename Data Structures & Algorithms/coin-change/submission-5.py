class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BRUTE FORCE
        # O(n^(amount/min value in coins))
        # O(amount/min value in coins)
        # def dfs(rem): #returns num of coins from this current amount to reach amount of zero
        #     if rem == 0:
        #         return 0
        #     if rem < 0:
        #         return float('inf')
            
        #     best = float('inf')
        #     for c in coins:
        #         best = min(best, dfs(rem - c))

        #     return 1 + best

        # minCoins = dfs(amount)
        # return minCoins if minCoins != float('inf') else -1
        
        # Memoisation DP top down
        
        # Time: num states * work per state: O(amount * n)
        # Space: memo dict holds all amounts: O(amount)

        memo = {} # an amount of coins -> the num of coins from this amount to reach amount of zero

        def dfs(rem): #returns num of coins from this current amount to reach amount of zero
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            
            if rem in memo:
                return memo[rem]

            best = float('inf')
            for c in coins:
                best = min(best, dfs(rem - c))

            memo[rem] = 1 + best
            return memo[rem]

        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1