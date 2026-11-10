class Solution:
    def rob(self, nums: List[int]) -> int:
   
        memo = {} # house -> total money from this house to end of street

        def dfs(house): # returns total money stolen from this house to end of street
            if house >= len(nums):
                return 0

            if house in memo:
                return memo[house]
            
            left = nums[house] + dfs(house + 2)
            right = dfs(house + 1)

            moneyToEnd = max(left, right)
            memo[house] = moneyToEnd

            return memo[house]

        return dfs(0)