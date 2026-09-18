class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]: 
                # left side is sorted - so trusted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # right hand side is sorted - so use this as trusted to do comparisons with
                if  nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1