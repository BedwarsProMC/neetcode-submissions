class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        countS1 = {}
        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)

        countS2 = {}
        l = 0
        for r in range(len(s2)):
            countS2[s2[r]] = 1 + countS2.get(s2[r], 0)
            if countS1 == countS2:
                return True
            elif (r - l + 1) == len(s1):
                # if we have a window size equal to len of s1
                freq = countS2.get(s2[l]) - 1
                if freq > 0:
                    countS2[s2[l]] = freq
                else:
                    countS2.pop(s2[l])
                l += 1
        return False