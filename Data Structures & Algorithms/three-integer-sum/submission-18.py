class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            # EARLY EXIT optimisaiton
            if nums[i] > 0:
                break

            # MUST be if NOT WHiLe as while infiintie loop with the continue acting on the while loop itself, NOT THE outer for lop
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip duplicate i values

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # EQUALS 0 - GOOD
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # SKIP LEFT DUPLICATES ALSO
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

            
        