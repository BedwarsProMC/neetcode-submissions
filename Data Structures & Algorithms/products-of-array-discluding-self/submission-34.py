class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        prefix_times_suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= prefix_times_suffix
            prefix_times_suffix *= nums[i]

        return res

