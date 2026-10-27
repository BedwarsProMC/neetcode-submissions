from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # T = len(tasks)
        # n = cooldown

        # Time: O(T * n)
        # Space: O(1) - dict, heap and q hold at most 26 items.

        count = {} # val -> freq
        for val in tasks: # O(T)
            count[val] = 1 + count.get(val, 0)
        
        max_heap = [-freq for freq in count.values()] # O(26) = O(1)
        heapq.heapify(max_heap) # O(26) = O(1)

        q = deque() # (cnt, task_released_at)
        time = 0

        # Time complexity: All tasks the same letter, e.g. ["A","A","A","A"] with a big cooldown. Every A needs n idles after it except the last: That’s (T - 1) * (n + 1) + 1 intervals, which is O(T · n)

        while max_heap or q: # runs O(T * n) time
            time += 1

            if max_heap:
                cnt = -heapq.heappop(max_heap) # O(log(26)) = O(1)
                cnt -= 1
                if cnt > 0:
                    q.append( (cnt, time + n) ) # O(1)
            else:
                # if no heap, then we MUST have a q for while loop to be running
                # so we are idle waiting for the queue so can jump the time forward
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(max_heap, -q.popleft()[0]) # O(log(26)) = O(1)
        
        return time
