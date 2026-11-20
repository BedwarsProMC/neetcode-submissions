class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {} # index -> ways to decode for string represented from this index to end of string

        def dfs(i): # returns num of ways to decode string startng from index i going to end of string
            if i in memo:
                return memo[i]

            # gone through whole string so found a way
            if i == len(s):
                return 1

            # invalid for a 1 digit or 2 digit num to be a 0
            # eg '0' invalid and '06' invalid so return 0 as base case
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1) 
            if i + 1 < len(s) and (
                (s[i] == '1') or
                (s[i] == '2' and s[i + 1] < '7')
            ):
                res += dfs(i + 2)

            memo[i] = res
            return memo[i]


        return dfs(0)

        