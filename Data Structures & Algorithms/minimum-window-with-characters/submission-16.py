class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''

        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have = 0 # items in window, matching tCount
        need = len(tCount) # unique items in tCount

        window = {}

        res = [-1, -1]
        resLength = float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in tCount:
                window[c] = 1 + window.get(c, 0)

                if tCount[c] == window[c]:
                    have += 1

                
            while have == need:
                # keep moving left until have != need

                if (r - l + 1) < resLength:
                    # new smallest
                    res = [l, r]
                    resLength = r - l + 1

                if s[l] in tCount:
                    window[s[l]] -= 1

                    if window[s[l]] < tCount[s[l]]:
                        have -= 1

                l += 1
        
        [l, r] = res
        return s[l:r + 1] if resLength != float('infinity') else ''







        