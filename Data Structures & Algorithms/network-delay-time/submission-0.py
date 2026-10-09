class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = [[] for _ in range(n + 1)]
        for n1, n2, w in times:
            adj_list[n1].append([n2, w])
        
        min_heap = [[0, k]]
        time = 0
        visited = set()

        while min_heap:
            d, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            time = d

            for nei, w in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, [d + w, nei])
            
        return time if len(visited) == n else -1