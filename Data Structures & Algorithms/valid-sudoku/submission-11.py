class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == '.':
                    continue

                if value in rows[r]:
                    return False

                if value in cols[c]:
                    return False

                key = (r // 3, c // 3)
                # key = (r / 3) * 3 + (c / 3)

                if value in squares[key]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[key].add(value)
        
        return True