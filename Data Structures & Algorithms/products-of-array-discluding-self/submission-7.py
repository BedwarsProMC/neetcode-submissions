class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num: # anything not a ZERO
                prod *= num
            else: # THIS number is a Zero
                zero_count += 1

        if zero_count > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count:
                # if 1 or more
                res[i] = 0 if c else prod

            else:
                res[i] = prod // c
         
        return res