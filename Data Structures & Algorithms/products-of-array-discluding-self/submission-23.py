class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixes = [0] * len(nums)
        suffixes = [0] * len(nums)
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefixes[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            suffixes[i] = suffix
            suffix *= nums[i]

        for i in range(len(nums)):
            res[i] = prefixes[i] * suffixes[i]

        return res