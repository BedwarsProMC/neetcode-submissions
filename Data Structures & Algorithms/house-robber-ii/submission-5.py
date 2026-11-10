class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)

        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(house, maxHouse):
            if house >= maxHouse:
                return 0

            if house in memo:
                return memo[house]
            
            left = nums[house] + dfs(house + 2, maxHouse)
            right = dfs(house + 1, maxHouse)
            
            moneyToEnd = max(left, right)
            memo[house] = moneyToEnd
            return memo[house]
        
        result1 = dfs(0, len(nums) - 1)
        memo = {}

        
        result2 = dfs(1, len(nums))

        return max(result1, result2)

        