class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)

        self.min_heap = nums
        self.k = k

        while self.min_heap and len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
        
