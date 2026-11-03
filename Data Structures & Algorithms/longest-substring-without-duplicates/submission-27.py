class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()

        longest = 0 
        l = 0
        for r in range(len(s)):

            if s[r] in window:
                index = window.get(s[r]) + 1
                l = max(l, index)
            
            window[s[r]] = r

            longest = max(longest, r - l + 1)

        return longest 