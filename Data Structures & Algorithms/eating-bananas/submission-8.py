class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        minK = r
        while l <= r:
            k = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                # minK = min(minK, k)
                minK = k # we move right to be smaller in line below, so any future Ks will always be smaller so dont need a min check.
                r = k - 1
            else:
                l = k + 1
        
        return minK