class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for c in s1:
            need[c] = 1 + need.get(c, 0)

        required = len(need) # number of chars that we need to match at their specific frequency
        matches = 0 # incremented when a char matches AND has exact frequency

        window = {} # items currently in the window

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            window[c] = 1 + window.get(c, 0)
            if c in need and need[c] == window[c]:
                matches += 1

            if (r - l + 1) > len(s1):
                c = s2[l]
                if c in need and need[c] == window[c]:
                    matches -= 1
                window[c] -= 1
                l += 1

            if matches == required:
                return True

        return False


            
        