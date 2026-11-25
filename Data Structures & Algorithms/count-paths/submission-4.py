class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {} # (i, j) -> num paths from i,j to bottom corner

        def dfs(i, j): # returns num paths from i,j to bottom corner
            if i == m - 1 and j == n - 1:
                return 1
            
            if i == m or j == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            res = dfs(i, j + 1) + dfs(i + 1, j)
            memo[(i, j)] = res

            return memo[(i, j)]

        return dfs(0, 0)
        