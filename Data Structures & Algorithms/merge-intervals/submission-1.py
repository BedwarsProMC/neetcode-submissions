class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            previous = output[-1]
            if start <= previous[1]:
                previous[1] = max(previous[1], end)
            else:
                output.append([start, end])
        
        return output
        