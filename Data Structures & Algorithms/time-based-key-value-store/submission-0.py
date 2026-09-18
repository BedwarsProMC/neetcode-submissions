class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        array = self.map[key]

        l = 0 
        r = len(array) - 1
        res = ""
        while l <= r:
            m = l + (r-l) // 2

            if array[m][0] <= timestamp:
                res = array[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
            
        
