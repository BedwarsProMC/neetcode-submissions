class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # memo = {} # (i, j) -> num paths from i,j to bottom corner

        # def dfs(i, j): # returns num paths from i,j to bottom corner
        #     if i == m - 1 and j == n - 1:
        #         return 1
            
        #     if i == m or j == n:
        #         return 0

        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     res = dfs(i, j + 1) + dfs(i + 1, j)
        #     memo[(i, j)] = res

        #     return memo[(i, j)]

        # return dfs(0, 0)
        
        dp = [[0] * m for _ in range(n)]
        dp[n - 1][m - 1] = 1

        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                
                if j == n - 1 and i == m - 1:
                    continue
                    
                down = 0
                right = 0

                if j + 1 < n:
                    down = dp[j + 1][i]
                if i + 1 < m:
                    right = dp[j][i + 1]

                dp[j][i] = down + right

        return dp[0][0]

