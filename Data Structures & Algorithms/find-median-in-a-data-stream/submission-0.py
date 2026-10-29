class MedianFinder:

    def __init__(self):
        # Space: O(n) as both heaps contain together the n numbers

        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None: # Time: log(n)
        # add to small
        heapq.heappush(self.small, -num)

        # values in small MUST be <= values in large
        # so compare biggest in small to smallest in large
        if (self.small and self.large and \
            -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # the heaps must be equal length or diff of 1 of each other.
        if len(self.small) > len(self.large) + 1:
            # small too long
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            # large too long
             val = heapq.heappop(self.large)
             heapq.heappush(self.small, -val)

    def findMedian(self) -> float: # Time: O(1)
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2
        
        