class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TOP DOWN DP MEMOISATION.
        # memo = {} # a remaining value - > number of coins from this remaining value to reach 0

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
        # return res if res != float('inf') else -1 


        # Bottom-Up DP tabulation
        # Time: O(amount * len(coins))
        # Space: O(amount)

        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if (a - c) >= 0: # If the remaining is >=0 (if less than 0 we dont care about it as that is an overshoot)
        #             dp[a] = min(dp[a], 1 + dp[a - c])

        # res = dp[amount]
        # if res == amount + 1: return -1
        # return res



        # BFS approach we go down level by level and stop as soon as we reach ermaining of 0 which guarantees shortest path, use a visited set (which is like memo) becuase we dont want to explore from an amount again
        if amount == 0:
            return 0

        q = deque([amount])
        coinsUsed = 0

        visited = {amount} # set

        while q:
            coinsUsed += 1

            for _ in range(len(q)):
                nxt = q.popleft()
                
                for c in coins:
                    rem = nxt - c
                    
                    if rem == 0:
                        return coinsUsed

                    if rem >= 0 and rem not in visited:
                        visited.add(rem)
                        q.append(rem)

        return -1












