class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seem = dict() # char -> last seen index

        longest = 0 
        l = 0
        for r in range(len(s)):

            if s[r] in last_seem:
                index = last_seem[s[r]] + 1
                # if index larger than l then its in the window so move l up 1. 
                # otherwise its outdated so keep l where it is
                l = max(l, index)
            
            last_seem[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest 