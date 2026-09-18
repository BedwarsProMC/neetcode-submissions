class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        window = set()
        maxL = 0

        l = r = 0
        while r < len(s):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            length = (r - l) + 1
            maxL = max(maxL, length)
            r += 1

        return maxL