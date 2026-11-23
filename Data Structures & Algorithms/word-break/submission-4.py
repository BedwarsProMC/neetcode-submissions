class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp bottom up
        # O(n . m . t)
        # O(n)

        dp = [False] * (len(s) + 1) # each index i represents if can break from here to end of word.
        dp[len(s)] = True # at end of word we have successfully broken, so base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:

                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break
                
        return dp[0]