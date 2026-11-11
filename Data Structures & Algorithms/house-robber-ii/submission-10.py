class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def robLine(start, end):
            memo = {} # house -> total from this house to end of street
            def dfs(house):
                if house >= end:
                    return 0

                if house in memo:
                    return memo[house]

                rob = nums[house] + dfs(house + 2)
                skip = dfs(house + 1)

                totalToEnd = max(rob, skip)
                memo[house] = totalToEnd

                return memo[house]

            return dfs(start)

        if len(nums) == 1:
            return nums[0]
            
        return max(
            robLine(0, len(nums) -1),
            robLine(1, len(nums))
        )
