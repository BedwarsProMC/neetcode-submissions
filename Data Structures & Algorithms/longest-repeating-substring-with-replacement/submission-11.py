class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = dict()

        l = 0 
        maxF = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxF = max(maxF, window[s[r]])

            while (r-l+1) - maxF > k:
                window[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest