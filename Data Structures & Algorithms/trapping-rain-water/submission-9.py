class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        maxL = 0
        maxR = 0
        l = 0
        r = len(height) - 1

        while l <= r:
            if maxL <= maxR:
                vol = min(maxL, maxR) - height[l]
                total += max(0, vol)
                maxL = max(maxL, height[l])
                l += 1
            else:
                vol = min(maxL, maxR) - height[r]
                total += max(0, vol)
                maxR = max(maxR, height[r])
                r -= 1

        return total