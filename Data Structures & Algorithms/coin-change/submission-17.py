class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {} # rem -> min coins from this rem to reach 0

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
        if res == float('inf'):
            return -1
        return res
        