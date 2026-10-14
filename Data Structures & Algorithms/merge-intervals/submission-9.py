class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            last_end = res[-1][1]
            if start <= last_end:
                res[-1] = [
                    min(res[-1][0], start),
                    max(last_end, end)
                ]
            else:
                res.append(intervals[i])

        return res    