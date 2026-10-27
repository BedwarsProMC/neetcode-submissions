# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # max heap

#         # Time: O(n + klogn)
#         heap = [-i for i in nums]
#         heapq.heapify(heap) # O(n)

#         for _ in range(k-1): # O(k * logn)
#             heapq.heappop(heap)
        
#         return -heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # COUNTING SORT

        # Values are limited to -1000..1000, so only 2001 possible values.
        # Count each value, then walk down from the largest until we reach the kth.
        # Time: O(n + 2001) = O(n)
        # Space: O(2001) = O(1), at most one key per distinct value

        count = {} # val -> freq
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for value in range(1000, -1001, -1):
            value_freq = count.get(value, 0)
            k -= value_freq

            # when hit the value where k is 0 (or goes below) we at kth largest element.
            if k <= 0:
                return value

