class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # O(2^n) TOO INEFFICIENT TIMES OUT

        total = sum(nums) # if total is odd. then half of total will NOT be an integer so impossible to sum to with just integers

        if total % 2 == 1:
            # if the total is odd, halving will NOT give INT
            return False

        target = total // 2

        def dfs(i, t): # returns whether the sum of the elements from i onwards can make t
            if t == 0:
                return True
            if i == len(nums) or t < 0:
                return False

            # TODO memo

            # TAKE or SKIP
            res = dfs(i + 1, t - nums[i]) or dfs(i + 1, t)
            # memo[(i, t)] = res
            # return memo[(i, t)]
            return res

        return dfs(0, target)
