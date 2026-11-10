class Solution:
    def climbStairs(self, n: int) -> int:

        # top down        
        # memo = {} # step -> num of ways from this step to top

        # def dfs(step):
        #     if step == n:
        #         return 1
        #     if step > n:
        #         return 0
        #     if step in memo:
        #         return memo[step]

        #     left = dfs(step + 1)    
        #     right = dfs(step + 2)

        #     memo[step] = left + right
        #     return memo[step]
        
        # return dfs(0)

        # bottom up
        dp = [0] * (n + 2)
        dp[n] = 1
        dp[n + 1] = 0

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]

        
