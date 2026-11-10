class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def rob_line(start, end):

            memo = {}
            def dfs(house):
                if house >= end:
                    return 0

                if house in memo:
                    return memo[house]

                rob = nums[house] + dfs(house + 2)
                skip = dfs(house + 1)
                moneyToEnd = max(rob, skip)
                memo[house] = moneyToEnd
                return memo[house]
                
            return dfs(start)

        return max(
            rob_line(0, len(nums) - 1),
            rob_line(1, len(nums))
        )
