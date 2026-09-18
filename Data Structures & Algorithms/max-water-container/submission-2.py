class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1

        maxVolume = -1

        while l < r:
            vol = (r - l) * min(heights[l], heights[r])

            maxVolume = max(vol, maxVolume)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxVolume

