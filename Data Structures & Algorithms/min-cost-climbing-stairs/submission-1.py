class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {} # step -> cost to top of stairs from this step

        def dfs(step): # returns cost to top from current step
            if step >= len(cost):
                return 0

            if step in memo:
                return memo[step]

            left = dfs(step + 1)
            right = dfs(step + 2)

            costToTop = cost[step] + min(left, right)
            memo[step] = costToTop

            return costToTop

        return min(dfs(0), dfs(1))
        