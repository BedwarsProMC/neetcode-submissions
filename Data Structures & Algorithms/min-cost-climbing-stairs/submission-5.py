class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one = cost[n - 1]
        two = 0

        for i in range(n - 2, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp

        return min(one, two)