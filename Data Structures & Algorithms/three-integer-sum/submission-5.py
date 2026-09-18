class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn
        res = []
        
        i = 0
        while i < (len(nums) - 2): # n^2
            l = i + 1
            r = len(nums) - 1

            # do a 2 sum
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]

                if currentSum < 0:
                    l += 1
                elif currentSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

            i += 1
            while nums[i] == nums[i - 1] and i < len(nums) - 2:
                i += 1
        
        return res
