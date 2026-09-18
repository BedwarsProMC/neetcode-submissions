class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        for c in s:
            sCount[c] = 1 + sCount.get(c, 0)

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        return sCount == tCount
