class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        total = 0

        maxL = height[l]
        maxR = height[r]

        while l < r:

            if maxL <= maxR:
                l += 1
                total += max(0, min(maxL, maxR) - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                total += max(0, min(maxL, maxR) - height[r])
                maxR = max(maxR, height[r])

        return total
        