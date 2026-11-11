class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # def robLine(start, end):
        #     memo = {} # house -> total from this house to end of street
        #     def dfs(house):
        #         if house >= end:
        #             return 0

        #         if house in memo:
        #             return memo[house]

        #         rob = nums[house] + dfs(house + 2)
        #         skip = dfs(house + 1)

        #         totalToEnd = max(rob, skip)
        #         memo[house] = totalToEnd

        #         return memo[house]

        #     return dfs(start)

        if len(nums) == 1:
            return nums[0]

        def helper(start, end):
            one = nums[end]
            two = 0

            for i in range(end - 1, start - 1, -1):
                temp = one
                one = max(nums[i] + two, one)
                two = temp

            return one



        n = len(nums)
        return max(
            helper(0, n - 2),
            helper(1, n - 1)
        )


