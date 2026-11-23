class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # exponential:
        # O(m^n . t)
        # O(n)

        # top down memoization dp
        # O(n.m.t)
        # O(n)

        memo = {} # index -> can we break from this index to the end of the word?

        def dfs(i):
            if i in memo:
                return memo[i]

            # base case. reach end of word then: yes
            if i == len(s):
                return True


            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    
                    if dfs(i + len(word)):
                        
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)