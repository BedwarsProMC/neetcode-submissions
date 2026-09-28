class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        # visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for rd, cd in directions:
                    row, col = r + rd, c + cd

                    if row < 0 or row >= rows or \
                        col < 0 or col >= cols or \
                        grid[row][col] != 2147483647: # (row, col) in visited or 
                        continue

                    grid[row][col] = level
                    q.append((row, col))
                    # visited.add(( row, col))

            level += 1

        