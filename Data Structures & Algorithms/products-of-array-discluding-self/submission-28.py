class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num

        res = [0] * len(nums)

        # 2 zeros, all zero.
        if zero_cnt > 1: return res


        # 1, or 0 zero 
        for i in range(len(nums)):
            if zero_cnt == 0:
                # no zeros
                res[i] = prod // nums[i]
            else:
                # 1 zero in da array broski
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0

        return res

            