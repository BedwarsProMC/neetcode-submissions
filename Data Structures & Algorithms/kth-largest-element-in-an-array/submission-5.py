class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        target = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]          # use the last element as the pivot
            p = l                    # where the next "small" number goes

            # move everything <= pivot to the left
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # put the pivot just after all the small numbers
            nums[p], nums[r] = nums[r], nums[p]

            # pivot is now at its final sorted position, p
            if p > target:
                return quickSelect(l, p - 1)    # answer is on the left
            elif p < target:
                return quickSelect(p + 1, r)    # answer is on the right
            else:
                return nums[p]                  # found it

        return quickSelect(0, len(nums) - 1) 