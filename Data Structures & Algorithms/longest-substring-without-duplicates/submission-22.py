class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = {} # char -> last index

        l = 0
        for r in range(len(s)):

            if s[r] in window:
                l = max(window[s[r]] + 1, l)

            # window.add(s[r])

            window[s[r]] = r
            longest = max(longest, r - l + 1)

        return longest