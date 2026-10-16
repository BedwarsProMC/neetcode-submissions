class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # { 0 -> set() } row number to set of nums
        cols = defaultdict(set) # { 4 -> set() } col number to set of nums
        squares = defaultdict(set) # { (r//3, c//3) -> set() } square to set of nums

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                if value == ".":
                    continue
                
                if value in rows[r] or \
                    value in cols[c] or \
                    value in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)
            
        return True