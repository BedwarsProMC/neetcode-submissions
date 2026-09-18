class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        t = 0
        b = ROWS - 1
        while t <= b:
            row = t + (b - t) // 2
            
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break 

        if not t <= b:
            return False

        row = t + (b-t) // 2

        l = 0
        r = COLS - 1
        while l <= r:
            m = l + (r-l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False