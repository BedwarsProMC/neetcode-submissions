class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = {} # {char -> index}
        maxL = 0
        
        l = 0
        for r in range(len(s)):
            
            if s[r] in window:
                index = window[s[r]] + 1
                l = max(index, l)
            
            window[s[r]] = r
            maxL = max(maxL, (r - l) + 1)

        return maxL