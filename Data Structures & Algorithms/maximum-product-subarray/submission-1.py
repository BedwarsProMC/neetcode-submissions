class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]

        for i in range(len(nums)):
            cand = (nums[i], nums[i] * curMin, nums[i] * curMax)
            curMin, curMax = min(cand), max(cand)
            res = max(res, curMax)

        return res