class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming bottom-up (tabulation)
        # space optimised. only need to keep last 2 values

        one = 1
        two = 0

        for step in range(n - 1, -1, -1):
            temp = one
            one = one + two
            two = temp
        return one
