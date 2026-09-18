class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {} # char -> count
        longest = 0

        l = 0
        maxF = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            maxF = max(maxF, window[s[r]])

            while (r - l + 1) - maxF > k:
                window[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))

        return longest
