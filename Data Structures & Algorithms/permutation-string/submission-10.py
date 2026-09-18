class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}
        required = len(need)
        matches = 0
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                matches += 1

            if r - l + 1 > len(s1):
                c = s2[l]
                if c in need and window[c] == need[c]:
                    matches -= 1
                window[c] -= 1
                l += 1

            if matches == required:
                return True

        return False