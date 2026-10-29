import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quickSelect
        # O(n) average time as with a random pivot we half the search on average each time so start of doign n then n/2 then n/4 = 2n = O(n)
        # worse case we remove 1 item eg reverse sorted array so O(n^2)

        k = len(nums) - k

        def quickSelect(lo, hi):
            # using always right as pivot: pivot = nums[hi]
            # using random pivot:
            r = random.randint(lo, hi)
            # move random pivot to end
            nums[hi], nums[r] = nums[r], nums[hi]

            pivot = nums[hi]

            i = lo
            for j in range(lo, hi):
                if nums[j] <= pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[hi], nums[i] = nums[i], nums[hi]

            # pivot at index i now
            if k > i: return quickSelect(i + 1, hi)
            if k < i: return quickSelect(lo, i - 1)
            return nums[i]
        
        return quickSelect(0, len(nums) - 1)