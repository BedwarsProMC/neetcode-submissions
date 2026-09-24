class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            grid[r][c] = '0'
            q = deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()

                directions = [(0,1),(0,-1),(1,0),(-1,0)]

                for rd, cd in directions:
                    r, c = row + rd, col + cd

                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == "1": # and not visited
                        q.append((r,c))
                        grid[r][c] = "0"
    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": # and not visited
                    islands += 1
                    bfs(r, c)

        return islands
        