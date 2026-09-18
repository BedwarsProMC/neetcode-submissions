class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {} # char -> count

        longest = 0

        l = 0
        for r in range(len(s)):

            window[s[r]] = 1 + window.get(s[r], 0)
            length = (r - l) + 1

            while length - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
                length = (r - l) + 1
            
            longest = max(longest, length)

        return longest
