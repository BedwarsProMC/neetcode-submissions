class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # # Recursive exponential - Should TIME OUT AND NOT RUN
        # # O(2^n) as that many subsets 
        # # O(n)

        # def dfs(i): # returns the LIS from this index onwards to the end, including this index
        #     # implicit BASE CASE 1: out of bounds, so doesnt dfs again
        #     # implicit BASE CASE 2: end of arr, so returns the 1

        #     LIS = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > nums[i]:
        #             LIS = max(LIS, 1 + dfs(j))

        #     return LIS

        
        # # sequence could start from any of the indices
        # best = 0
        # for i in range(len(nums)):
        #     best = max(best, dfs(i))
        # return best



        # Top down memoisation dp solution
        # O(n . n) time
        # O(n) space

        memo = {} # index -> the LIS from this index (including this index) onwards to the end

        def dfs(i): # returns the LIS from this index onwards to the end, including this index
            # implicit BASE CASE 1: out of bounds, so doesnt dfs again
            # implicit BASE CASE 2: end of arr, so returns the 1

            if i in memo:
                return memo[i]

            LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[i] = LIS
            return memo[i]

        
        # sequence could start from any of the indices
        best = 0
        for i in range(len(nums)):
            best = max(best, dfs(i))
        return best



        # DYNAMIC PROGRAMMING BOTTOM-up TABULATION approach
        # Time: O(n.n)
        # Space O(n)
        dp = [1] * len(nums)
        # LIS = 1
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    # LIS = max(LIS, dp[i])
        # return LIS
        return max(dp)

        

























