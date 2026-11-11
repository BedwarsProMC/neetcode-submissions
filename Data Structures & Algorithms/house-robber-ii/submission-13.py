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

        def helper(arr):
            n = len(arr)
            one = arr[n - 1]
            two = 0

            for i in range(n - 2, -1, -1):
                temp = one
                one = max(arr[i] + two, one)
                two = temp

            return one


        if len(nums) == 1:
            return nums[0]

        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )


