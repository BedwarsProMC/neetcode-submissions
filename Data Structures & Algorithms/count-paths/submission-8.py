class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # decision tree
        # time: O(2 ^ (m + n))
        # space: O(m + n)

        # top down memoisation
        # time: O(m * n)
        # space: O(m * n)
        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j): # returns num of ways from i, j to end
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]
            
            res = dfs(i + 1, j) + dfs(i, j + 1)
            memo[i][j] = res
            return res

        return dfs(0, 0)

        # bottom up tabulation
        # time: O(m * n)
        # space: O(m * n)

        # bottom up space optimised
        # time: O(m * n)
        # space: O(n)