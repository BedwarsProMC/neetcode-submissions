class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = [] # (index, value)

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                stackI, stackH = stack.pop()
                maxArea = max(maxArea, (i - stackI) * stackH)
                start = stackI

            stack.append([start, h])

        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (len(heights)-i) * h)

        return maxArea