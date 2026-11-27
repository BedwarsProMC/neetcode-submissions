class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # decision tree
        # Time: O(2 ^ (m + n))
        # Space: O(m + n)
        
        
        # then with memo
        # Time: O(m.n)
        # Space: O(m.n)

        # memo = {} # (i, j) -> length of LCS from text1[i:] and text2[j:]

        # def dfs(i, j): # returns length of LCS from ...
        #     if i == len(text1) or j == len(text2):
        #         return 0

        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if text1[i] == text2[j]:
        #         res = 1 + dfs(i + 1, j + 1)
        #     else:
        #         res = max(dfs(i + 1, j), dfs(i, j + 1))

        #     memo[(i, j)] = res
        #     return res

        # return dfs(0, 0)


        # bottom up
        # Time: O(m . n)
        # Space: O(m . n)

        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # for i in range(len(text1) -1, -1, -1):
        #     for j in range(len(text2) -1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        # return dp[0][0]
                
        # bottom up space optimised
        dp = [0] * (len(text2) + 1)
        
        for i in range(len(text1) -1, -1, -1):
            diag = 0
            for j in range(len(text2) -1, -1, -1):
                temp = dp[j]

                if text1[i] == text2[j]:
                    dp[j] = 1 + diag
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                
                diag = temp
                

        return dp[0]


