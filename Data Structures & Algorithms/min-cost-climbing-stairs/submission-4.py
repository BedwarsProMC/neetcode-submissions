class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) - 1
        one = cost[n]
        two = 0

        for i in range(n - 1, -1, -1):
            temp = one
            one = cost[i] + min(one, two)
            two = temp

        return min(one, two)