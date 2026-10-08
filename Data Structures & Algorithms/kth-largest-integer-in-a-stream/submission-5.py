class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums[:]
        self.k = k

        heapq.heapify(self.min_heap) # converts into a heap: O(n) time.

        # make the min heap only contain the top K numbers, so then the min item will be the kth largest item. Since we only add numbers, it is fine to discard the smallest.


        while len(self.min_heap) > self.k: # O((n − k) log n)
            heapq.heappop(self.min_heap)  # as eachh pop is log(n) operation

    def add(self, val: int) -> int:
        
        heapq.heappush(self.min_heap, val) # O(logk)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
        
