class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        area = 0
        while l < r:
            
            if height[l] <= height[r]:
                l += 1
                maxLeft = max(height[l], maxLeft)
                newArea = min(maxLeft, maxRight) - height[l]
                area += max(0, newArea)
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                newArea = min(maxLeft, maxRight) - height[r]
                area += max(0, newArea)

        return area