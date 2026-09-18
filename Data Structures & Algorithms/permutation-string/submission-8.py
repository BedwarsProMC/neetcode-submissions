class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = dict()

        for c in s1:
            s1map[c] = s1map.get(c, 0) + 1
        
        window = dict()

        l = 0
        r = 0

        while r < len(s1):
            # populate map initially to get right length
            window[s2[r]] =  window.get(s2[r], 0) + 1
            r += 1

        while r < len(s2):
            if window == s1map:
                return True

            window[s2[r]] = window.get(s2[r], 0) + 1

            if window.get(s2[l]) == 1:
                del window[s2[l]]
            else:
                window[s2[l]] = window.get(s2[l]) - 1

            l += 1
            r += 1


        return s1map == window
            

        