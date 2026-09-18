class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        windowSet = set()
        longest = 0
        
        l = r = 0
        while r < len(s):
            
            while s[r] in windowSet:
                
                windowSet.remove(s[l])
                l += 1


            
            windowSet.add(s[r])

            length = r - l + 1
            longest = max(longest, length)

            r += 1

        return longest