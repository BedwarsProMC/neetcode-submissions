class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # one = nums[n - 1]
        # two = 0

        # for i in range(n - 2, -1, -1):
        #     temp = one
        #     one = max(nums[i] + two, one)
        #     two = temp

        # return one

        n = len(nums)
        dp = [0] * (n + 1)
        dp[n- 1] = nums[n-1]
        dp[n] = 0

        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        return dp[0]

        