class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {} # step -> num of ways from this step to top

        def dfs(step):
            if step == n:
                return 1
            if step > n:
                return 0
            if step in memo:
                return memo[step]

            left = dfs(step + 1)    
            right = dfs(step + 2)

            memo[step] = left + right
            return memo[step]
        
        return dfs(0)