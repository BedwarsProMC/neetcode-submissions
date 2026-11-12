class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {} # a remaining value - > number of coins from this remaining value to reach 0

        def dfs(rem):
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

        res = dfs(amount)
        return res if res != float('inf') else -1 