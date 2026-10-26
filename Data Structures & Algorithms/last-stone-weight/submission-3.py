class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones) # min heap
        
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            if x < y:
                y = y - x
                heapq.heappush(stones, -y)

            elif y < x:
                x = x - y
                heapq.heappush(stones, -x)
            
            else:
                pass

        return -stones[0] if stones else 0