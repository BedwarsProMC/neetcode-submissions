class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                
                for rd, cd in directions:
                    r, c = row + rd, col + cd
                    
                    if r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in visited and grid[r][c] == '1':
                        q.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    bfs(r,c)

        return islands
        