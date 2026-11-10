class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        one = nums[n - 1]
        two = 0

        for i in range(n - 2, -1, -1):
            temp = one
            one = max(nums[i] + two, one)
            two = temp
        
        return one