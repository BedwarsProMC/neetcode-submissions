class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # O(2^n) recursive decision tree. adding memoisation brings it to O(n . target) time

        # total = sum(nums) # if total is odd. then half of total will NOT be an integer so impossible to sum to with just integers

        # if total % 2 == 1:
        #     # if the total is odd, halving will NOT give INT
        #     return False

        # target = total // 2

        # memo = {} # (i, t) -> if the elements from this index onwards can sum to the value of t

        # def dfs(i, t): # returns whether the sum of the elements from i onwards can make t
        #     if t == 0:
        #         return True
        #     if i == len(nums) or t < 0:
        #         return False

        #     if (i, t) in memo:
        #         return memo[(i, t)]

        #     # TAKE or SKIP
        #     res = dfs(i + 1, t - nums[i]) or dfs(i + 1, t)
        #     memo[(i, t)] = res
        #     return memo[(i, t)]

        # return dfs(0, target)



        # O(n. t) time bottom up dp
        # O(t) space, t is sum of array halved. 
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [False] * (target + 1) # dp[j] means is there a subset of numbers that sum up to j?
         
        dp[0] = True # Yes, no numbers sums up to zero, so base case.

        for num in nums:

            # work backwards so we dont take a number twice
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num] # skip num or take it if j - num was reachable

            # early exit
            if dp[target]:
                return True

        return dp[target]
