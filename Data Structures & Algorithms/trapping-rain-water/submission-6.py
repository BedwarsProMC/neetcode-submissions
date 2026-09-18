class Solution:
    def trap(self, height: List[int]) -> int:
        prefixes = [0] * len(height) #maximums
        suffixes = [0] * len(height) #maximums

        maxHeight = 0
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
            prefixes[i] = maxHeight
        
        maxHeight = 0
        for i in range(len(height) - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            suffixes[i] = maxHeight
        
        totalVol = 0
        for i in range(len(height)):
            vol = min(prefixes[i], suffixes[i]) - height[i]
            totalVol += max(0, vol)

        return totalVol
