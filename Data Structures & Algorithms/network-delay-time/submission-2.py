class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = [[] for _ in range(n + 1)]
        for ui, vi, ti in times:
            adj_list[ui].append([vi, ti])
        
        min_heap = [ (0, k) ]
        t = 0
        visited = set()

        while min_heap:
            d, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            t = d

            for nei, weight in adj_list[node]:
                heapq.heappush(min_heap, (d + weight, nei))
        
        return t if len(visited) == n else -1