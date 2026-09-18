class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        need = {}
        for c in s1:
            need[c] = 1 + need.get(c, 0)
        
        required = len(need)
        matches = 0

        window = {} # char -> count

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            window[c] = 1 + window.get(c, 0)
            if c in need and window[c] == need[c]:
                matches += 1

            if (r - l + 1) > len(s1):
                c = s2[l]
                if c in need and window[c] == need[c]:
                    matches -= 1
                window[c] -= 1
                l += 1
            
            if required == matches:
                return True

        return False