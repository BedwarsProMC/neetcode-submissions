class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prefixes = [0] * n
        prefix = 1
        for i in range(n):
            prefixes[i] = prefix
            prefix *= nums[i]

        suffixes = [0] * n
        suffix = 1
        for i in range(n - 1, -1, -1):
            suffixes[i] = suffix
            suffix *= nums[i]

        res = [0] * n
        for i in range(n):
            res[i] = prefixes[i] * suffixes[i]

        return res

