from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {} # val -> freq
        for val in tasks:
            count[val] = 1 + count.get(val, 0)
        
        max_heap = [-freq for freq in count.values()] # O(26)
        heapq.heapify(max_heap) # O(n)

        q = deque() # (cnt, task_released_at)
        time = 0
        while max_heap or q:
            time += 1

            if max_heap:
                cnt = -heapq.heappop(max_heap)
                cnt -= 1
                if cnt > 0:
                    q.append( (cnt, time + n) )

            if q and q[0][1] == time:
                heapq.heappush(max_heap, -q.popleft()[0])
        
        return time
