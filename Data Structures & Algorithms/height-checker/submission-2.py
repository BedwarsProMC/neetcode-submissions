class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        # expected = sorted(heights) # O(nlogn)
        
        # count sort in O(n + k) time (k=100): O(n) time.
    
        count = [0] * 101 # each index is height, with value being freq
        for h in heights:
            count[h] += 1

        # now loop forward along array to build a sorted in O(n + k) 
        # time where K = 100
        expected = []
        for h in range(1, 101):
            freq = count[h]
            for _ in range(freq):
                expected.append(h)
            
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res