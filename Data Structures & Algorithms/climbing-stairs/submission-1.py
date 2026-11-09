class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {} # total -> num paths 

        def dfs(total):
            if total > n:
                return 0
            if total == n:
                return 1
            
            if total in cache:
                return cache[total]

            left = dfs(total + 1)
            right = dfs(total + 2)
            
            cache[total] = left + right

            return left + right

        return dfs(0)