class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones) # max heap
        
        while len(stones) > 1:
            first = -1 * heapq.heappop(stones) # bigest or equal to second
            second = -1 * heapq.heappop(stones) # smaller or equal to first

            if second < first:
                diff = first - second
                heapq.heappush(stones, -diff)

        return -stones[0] if stones else 0