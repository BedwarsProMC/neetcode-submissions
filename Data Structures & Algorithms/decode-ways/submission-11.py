class Solution:
    def numDecodings(self, s: str) -> int:
        # O(n)
        # O(n)

        # memo = {} # index -> ways to decode 

        # def dfs(i): # returns num of ways to decode the string represetned FROM index i to end of string.
        #     if i in memo:
        #         return memo[i]

        #     if i == len(s):
        #         return 1
        #     if s[i] == '0':
        #         return 0
            
        #     res = dfs(i + 1)
        #     if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
        #         res += dfs(i + 2)

        #     memo[i] = res
        #     return memo[i
        #     ]
        
        # return dfs(0)

        # dp bottom up
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp[i] = dp[i] + dp[i + 2]

        return dp[0]


        # dp bottom up space optimised
        dp = 0
        dp1 = 1
        dp2 = 0

        for i in range(len(s) -1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1

            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                dp = dp + dp2

            dp, dp1, dp2 = 0, dp, dp1

        return dp1
            







