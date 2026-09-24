class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))

            height = heights[r][c]
            dfs(r - 1, c, visited, height)
            dfs(r + 1, c, visited, height)
            dfs(r, c - 1, visited, height)
            dfs(r, c + 1, visited, height)

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res