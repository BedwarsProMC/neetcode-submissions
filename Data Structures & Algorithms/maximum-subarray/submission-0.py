class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxRes = nums[0] # cant initalise to 0 as array could hold one negative number.\
        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            maxRes = max(maxRes, currSum)
        return maxRes