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
        # counting sort
        # 10,000 items so linear time is fine
        # each value is one of 2001 values so this constricted range means counting sort

        # Time: O(n + 2001)
        # Space: O(n)

        count = {} # val -> freq
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for i in range(1000, -1001, -1):
            numFreq = count.get(i, 0)
            k -= numFreq
            if k <= 0:
                return i

