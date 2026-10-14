class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by intervals end so we always have the furthest left ending interval first. so then if any future interval overlaps we know the original interval will end before this new one, so can discard the new interval completely.


        intervals.sort(key=lambda pair: pair[1])
        res = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd:
                res += 1
            else:
                prevEnd = end
        
        return res
