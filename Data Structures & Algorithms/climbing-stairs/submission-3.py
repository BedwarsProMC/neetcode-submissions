class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Time: O(n) as each value to n computed and saved, later calls O(1) for each.
        # Space: O(n) cache and recursion space

        memo = {} # total -> num paths 

        def dfs(total):
            if total > n:
                return 0
            if total == n:
                return 1

            # memoization - read
            if total in memo:
                return memo[total]

            left = dfs(total + 1)
            right = dfs(total + 2)
            
            # memoization - save it
            memo[total] = left + right

            return memo[total]

        return dfs(0)