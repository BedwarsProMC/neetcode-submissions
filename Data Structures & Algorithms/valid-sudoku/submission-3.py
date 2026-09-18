class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                value = board[r][c]

                # base cases
                if value == '.':
                    continue

                if (value in rows[r] or
                    value in cols[c] or
                    value in squares[(r // 3, c // 3)]):
                    return False


                # update sets
                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)

        return True
        