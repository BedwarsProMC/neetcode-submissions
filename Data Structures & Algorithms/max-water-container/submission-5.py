class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        l = 0 
        r = len(heights) - 1
        while l < r:
            vol = min(heights[l], heights[r]) * (r  - l)
            maxVol = max(maxVol, vol)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxVol