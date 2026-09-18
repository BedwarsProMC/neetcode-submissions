class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        for c in s1:
            need[ord(c) - ord('a')] += 1

        window = [0] * 26
        required = sum(1 for x in need if x > 0)
        matches = 0
        l = 0

        for r in range(len(s2)):
            i = ord(s2[r]) - ord('a')
            window[i] += 1
            if need[i] > 0 and window[i] == need[i]:
                matches += 1

            if r - l + 1 > len(s1):
                i = ord(s2[l]) - ord('a')
                if need[i] > 0 and window[i] == need[i]:
                    matches -= 1
                window[i] -= 1
                l += 1

            if matches == required:
                return True

        return False