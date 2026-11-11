class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * (n + 1)
        dp[n - 1] = cost[n - 1]
        dp[n] = 0

        for i in range(n - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
    
        # n = len(cost)
        # one = cost[n - 1]
        # two = 0

        # for i in range(n - 2, -1, -1):
        #     temp = one
        #     one = cost[i] + min(one, two)
        #     two = temp

        # return min(one, two)